from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import  CustomerForm, VendorForm, BuyOnDebtForm, ProductSoldForm, NotesForm, ProductForm, SignUpForm, LoginForm, UpdateProfileForm, UpdateUserForm
from .models import  Customer, Vendor, Notes, Product, ProductSold, Profile, BuyOnDebt, User
from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.conf import settings
import socketserver, json
from wsgiref import handlers
from datetime import date, timedelta
import datetime
from django.utils import timezone

# Demo mode imports
from .demo_utils import get_demo_objects_for_model, is_demo_mode
from .demo_data import get_demo_user, get_demo_profile, get_demo_vendor

socketserver.BaseServer.handle_error = lambda *args, **kwargs: None
handlers.BaseHandler.log_exception = lambda *args, **kwargs: None

def index(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    return render(request, 'mnotes/index.html')

def takenoteview(request):
    return HttpResponse("Entered text : " + str(request.POST.get('nametest')))

@login_required
def savednotes(request):
    notes_list = Notes.objects.filter(user=request.user)

    return render(request, 'mnotes/savednotes.html', {'notes_list' : notes_list} )

@login_required
def inventory(request):
    if is_demo_mode():
        # Use demo data
        product_list = get_demo_objects_for_model('Product')
        username = get_demo_user()
        user_props = get_demo_profile(username)
    else:
        # Use real database
        product_list = Product.objects.filter(user=request.user)
        username = User.objects.get(pk=request.user.id)
        user_props = Profile.objects.get(user=request.user)
    
    context = {'product_list' : product_list, 'user_name' : username, 'user_props' :  user_props}
    return render(request, 'mnotes/vendorpages/inventory.html', context)

@login_required
def takenote(request):
    form = NotesForm()
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            #note_text = form.cleaned_data.get('note_text')
            pub_date = form.cleaned_data.get('pub_date')
            nametestvalue = form.cleaned_data.get('nametest')
            form.save()

            return redirect(to='/takenoteview/')
        
    context = {'form' : form}
    return render(request, 'mnotes/takenote.html', context)

@login_required
def createproduct(request):
    if request.method == 'POST':
        if is_demo_mode():
            messages.warning(request, 'Bu demo rejim. Ma\'lumotlar saqlanmaydi. Real tizimda bu mahsulot yaratilgan bo\'lar edi.')
            return redirect('/inventory/')
            
        form = ProductForm(request.POST, request.FILES)
        BuyDebtForm = BuyOnDebtForm(request.POST)
        
        if form.is_valid() and BuyDebtForm.is_valid():
            product_name = form.cleaned_data.get('product_name')
            product_price_initial = form.cleaned_data.get('product_price_initial')
            product_price_told = form.cleaned_data.get('product_price_told')
            product_count = form.cleaned_data.get('product_count')
            product_color = form.cleaned_data.get('product_color')
            product_size = form.cleaned_data.get('product_size')
            product_season = form.cleaned_data.get('product_season')
            product_img = form.cleaned_data.get('product_img')
            isdebt = form.cleaned_data.get('isdebt')                
            owner_name = BuyDebtForm.cleaned_data.get('owner_name')
            owner_phone = BuyDebtForm.cleaned_data.get('owner_phone')
            ispartlypaid = BuyDebtForm.cleaned_data.get('ispartlypaid')
            paid_amount = BuyDebtForm.cleaned_data.get('paid_amount')
            isfullypaid = BuyDebtForm.cleaned_data.get('isfullypaid')


            if(paid_amount is None):
                paid_amount = 0
                left_amount = 0
            else:
                left_amount = product_count * product_price_initial - paid_amount

            due_date = BuyDebtForm.cleaned_data.get('due_date')
            product = form.save(commit=False)
            product.user = request.user
            user = form.cleaned_data.get('user')
            product.save()

            if isdebt == True:
                BuyOnDebt.objects.create(username=product.user, product_name=product_name, product_bought_count=product_count, product_bought_price=product_price_initial, owner_name=owner_name, owner_phone=owner_phone, due_date=due_date, paid_amount=paid_amount, left_amount=left_amount, isfullypaid=isfullypaid, ispartlypaid=ispartlypaid)

            messages.success(request, 'Mahsulot muvaffaqiyatli yaratildi')
            return redirect('/inventory/')
    else:
        form = ProductForm()
        BuyDebtForm = BuyOnDebtForm()
    context = {'form' : form, 'BuyDebtForm' : BuyDebtForm}
    return render(request, 'mnotes/vendorpages/createproduct.html', context)

def productview(request, id):
    if is_demo_mode():
        product_props = get_demo_objects_for_model('Product').filter(pk=id)
    else:
        product_props = Product.objects.filter(user=request.user, pk=id)
    
    context = {'product_props' : product_props}
    return render(request, 'mnotes/vendorpages/productview.html', context)

def selldebtview(request, id):
    selldebt_props = ProductSold.objects.get(username=request.user, pk=id, isdebt=True)


    # for sl in soldproduct_list:
    #     if(sl.isdebt):
    #         sellondebt_list.append(sl)

    context = { 'selldebt_props' : selldebt_props }
    return render(request, 'mnotes/vendorpages/selldebtview.html', context)

def buydebtview(request, id):
    buydebt_props = BuyOnDebt.objects.get(username=request.user, pk=id)

    context = {'buydebt_props' : buydebt_props }
    return render(request, 'mnotes/vendorpages/buydebtview.html', context)


# def searchselldebtselect(request):
#     if request.method == 'POST':
#         searched = request.POST['searched']
#         selldebt = Product.objects.filter(product_name__contains=searched, username=request.user)
#     else:
#         searched = ""
#         selldebt = ""
#     context = { 'searched' : searched, 'selldebt' : selldebt}
#     return render(request, 'mnotes/searchselldebtselect.html', context)

def selectsoldproduct(request):
    product_list = Product.objects.filter(user=request.user)
    
    context = { 'product_list' : product_list }
    return render(request, 'mnotes/vendorpages/selectsoldproduct.html', context)

def deleteproduct(request, id):

    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(request, 'Mahsulot muvaffaqiyatli o`chirildi')
    return redirect('inventory')

def productsold(request, id):
    product = Product.objects.get(pk=id, user=request.user)
    if request.method == 'POST':
        SoldProductForm = ProductSoldForm(request.POST)
        
        if SoldProductForm.is_valid():

            sold_price = SoldProductForm.cleaned_data.get('product_sold_price')
            sold_count = SoldProductForm.cleaned_data.get('product_sold_count')
            isdebt = SoldProductForm.cleaned_data.get('isdebt')
            user = request.user
            product_name = product.product_name
            customer_name = SoldProductForm.cleaned_data.get('customer_name')
            customer_phone = SoldProductForm.cleaned_data.get('customer_phone')
            due_date = SoldProductForm.cleaned_data.get('due_date')
            isfullypaid = SoldProductForm.cleaned_data.get('isfullypaid')
            ispartlypaid = SoldProductForm.cleaned_data.get('ispartlypaid')
            paid_amount = SoldProductForm.cleaned_data.get('paid_amount')

            if(paid_amount is None):
                paid_amount = 0
                left_amount = 0
            else:
                left_amount = sold_count * sold_price - paid_amount


            initial_price = product.product_price_initial
            initial_count = product.product_count


            if(sold_price < initial_price):
                messages.warning(request, 'Siz bu mahsulotni tan narxidan arzonga berdingiz!')

            if(sold_count > initial_count):
                messages.warning(request, 'Sizda bu miqdorda mahsulot mavjud emas!')
                profit = 0
            else:
                last_count = initial_count - sold_count
                product.product_count = last_count
                product.sold_count += sold_count
                product.save()

                profit = (sold_price - initial_price)*sold_count

                if(isdebt):                
                    isfullypaid = False
                    ProductSold.objects.create(product_name=product_name, username=request.user, 
                        product_sold_price=sold_price, product_sold_count=sold_count, 
                        profit=profit, isdebt=isdebt, isfullypaid=isfullypaid, ispartlypaid=ispartlypaid,
                        customer_name=customer_name, customer_phone=customer_phone, due_date=due_date,
                        paid_amount=paid_amount, left_amount=left_amount
                        )
                else:
                    isfullypaid = True
                    ispartlypaid = False
                    ProductSold.objects.create(product_name=product_name, username=request.user, product_sold_price=sold_price, 
                        product_sold_count=sold_count, profit=profit, isdebt=isdebt,
                        isfullypaid=isfullypaid, ispartlypaid=ispartlypaid, customer_name=customer_name, 
                        customer_phone=customer_phone, due_date=due_date, paid_amount=paid_amount, 
                        left_amount=left_amount) 
                
                messages.success(request, 'Sotilgan mahsulot muvaffaqiyatli saqlandi.')
                return redirect('soldproducts')
        else:
            profit = 0
    else:
        SoldProductForm = ProductSoldForm() 
        profit = 0

    
    context = {'product' : product, 'SoldProductForm' : SoldProductForm}    
    return render(request, 'mnotes/vendorpages/productsold.html', context)

def editproduct(request, id):        
    product = Product.objects.get(pk=id)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product )
  
        if form.is_valid():
            
            product_img = form.cleaned_data.get('product_img')

            form.save()
            messages.success(request, 'Mahsulot muvaffaqiyatli yangilandi')
            product_id = str(id)
            
            url = "../productview/"
            return redirect(url + product_id)

    else:
        form = ProductForm(instance=product)


    context = {'product' : product, 'form' : form}
    return render(request, 'mnotes/vendorpages/editproduct.html', context)
    
def sellondebts(request):
    if is_demo_mode():
        soldproduct_list = get_demo_objects_for_model('ProductSold')
        product_list = get_demo_objects_for_model('Product')
    else:
        soldproduct_list = ProductSold.objects.filter(username=request.user)
        product_list = Product.objects.filter(user=request.user)
        
    sellondebt_list = []

    for sl in soldproduct_list:
        if(sl.isdebt):
            sellondebt_list.append(sl)


    context = {'sellondebt_list' : sellondebt_list, 'product_list' : product_list}
    return render(request, 'mnotes/vendorpages/sellondebts.html', context)

def buyondebts(request):
    if is_demo_mode():
        buyondebt_list = get_demo_objects_for_model('BuyOnDebt')
        product_list = get_demo_objects_for_model('Product')
    else:
        buyondebt_list = BuyOnDebt.objects.filter(username=request.user)
        product_list = Product.objects.filter(user=request.user)

    context = {'buyondebt_list' : buyondebt_list, 'product_list' : product_list}
    return render(request, 'mnotes/vendorpages/buyondebts.html', context)


def selldebt(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = ProductSoldForm(request.POST)

        if form.is_valid():
            product_name = product.product_name
            product_sold_count = form.cleaned_data.get('product_sold_count')
            product_sold_price = form.cleaned_data.get('product_sold_price')
            customer_name = form.cleaned_data.get('customer_name')
            customer_phone = form.cleaned_data.get('customer_phone')
            due_date = form.cleaned_data.get('due_date')
            paid_amount = form.cleaned_data.get('paid_amount')


            if(paid_amount is None):
                paid_amount = 0
                left_amount = 0
                ispartlypaid = False
            else:
                ispartlypaid = True
                left_amount = product_sold_count * product_sold_price - paid_amount


            if(product_sold_count > product.product_count):
                messages.warning(request, 'Sizda bu miqdorda mahsulot mavjud emas!')
                profit = 0
            else:
                isfullypaid = False
                #updating the product's count and isdebt values in the database
                final_product_count = product.product_count + product_sold_count
                product.product_count = final_product_count
                product.isdebt = True
                product.save()

                profit = (product_sold_price - product.product_price_initial)*product_sold_count



                ProductSold.objects.create(username=request.user, product_name=product_name, product_sold_count=product_sold_count, product_sold_price=product_sold_price,
                                        customer_name=customer_name, customer_phone=customer_phone, due_date=due_date, paid_amount=paid_amount, 
                                        left_amount=left_amount, isdebt=True, ispartlypaid=ispartlypaid, isfullypaid=isfullypaid, profit=profit)
                messages.success(request, 'Qarzga berilgan mahsulot muvaffaqiyatli saqlandi.')
            return redirect('sellondebts')
    else:

        form = ProductSoldForm()
    context = {'product' : product, 'form' : form}
    return render(request, 'mnotes/vendorpages/selldebt.html', context)


def selldebtselect(request):
    product_list = Product.objects.filter(user=request.user)
    
    context = { 'product_list' : product_list }
    return render(request, 'mnotes/vendorpages/selldebtselect.html', context)



def returndebt(request, id):
    soldproduct = ProductSold.objects.get(pk=id)
    todays_date = timezone.now()
    soldproduct.isfullypaid = True
    soldproduct.ispartlypaid = False
    soldproduct.date_sold = todays_date
    soldproduct.save()
    messages.success(request, "Qarz muvaffaqiyatli to'landi")        
    return redirect('sellondebts')

def paydebt(request, id):
    debt = BuyOnDebt.objects.get(pk=id)
    debt.isfullypaid = True
    debt.ispartlypaid = False
    debt.save()
    messages.success(request, 'Qarz muvaffaqiyatli to`landi')
    return redirect('buyondebts')

def buydebt(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = BuyOnDebtForm(request.POST)
        if form.is_valid():
            paid_amount = form.cleaned_data.get('paid_amount')
            product_bought_count = form.cleaned_data.get('product_bought_count')
            product_bought_price = form.cleaned_data.get('product_bought_price')
            ispartlypaid = form.cleaned_data.get('ispartlypaid')
            due_date = form.cleaned_data.get('due_date')
            owner_name = form.cleaned_data.get('owner_name')
            owner_phone = form.cleaned_data.get('owner_phone')
            isfullypaid = False

            #updating the product's count and isdebt values in the database
            final_product_count = product.product_count + product_bought_count
            product.product_count = final_product_count
            product.isdebt = True
            product.save()

            if(paid_amount is None):
                paid_amount = 0
                left_amount = 0
            else:
                left_amount = product_bought_count * product_bought_price - paid_amount
            BuyOnDebt.objects.create(username=request.user, product_name=product.product_name, product_bought_count=product_bought_count, product_bought_price=product_bought_price, paid_amount=paid_amount, left_amount=left_amount, ispartlypaid=ispartlypaid, isfullypaid=isfullypaid, due_date=due_date, owner_name=owner_name, owner_phone=owner_phone)
            
            messages.success(request, 'Qarzga olingan mahsulot muvaffaqiyatli saqlandi.')
            return redirect('buyondebts')

    else:
        form = BuyOnDebtForm()

    context = {'form' : form, 'product' : product}
    return render(request, 'mnotes/vendorpages/buydebt.html', context)


def buydebtselect(request):
    product_list = Product.objects.filter(user=request.user)
    
    context = { 'product_list' : product_list }
    return render(request, 'mnotes/vendorpages/buydebtselect.html', context)

@login_required
def profile(request):
    if is_demo_mode():
        user_props = get_demo_profile(get_demo_user())
        vendor_props = get_demo_vendor(get_demo_user().username)
    else:
        user_props = Profile.objects.get(user=request.user)
        vendor_props = Vendor.objects.get(username=request.user)

    return render(request, 'mnotes/vendorpages/profile.html', {'user_props' : user_props, 'vendor_props' : vendor_props})


@login_required
def editprofile(request, username):
    user = Vendor.objects.get(username=username)

    if request.method == 'POST':
        vendor_Form = VendorForm(request.POST, instance=user)
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid() and vendor_Form.is_valid():
            user_form.save()
            profile_form.save()
            vendor_Form.save()
            messages.success(request, 'Akkountingiz muvaffaqiyatli yangilandi')
            return redirect('profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
        vendor_Form = VendorForm(instance=user)
    profile = Profile.objects.filter(user=request.user)
    context = { 'vendor_Form' : vendor_Form, 'user' : user, 'user_form' : user_form, 'profile_form' : profile_form, 'profile' : profile}
    return render(request, 'mnotes/vendorpages/editprofile.html', context)



class login(LoginView):
    form = LoginForm()


    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        if not remember_me:

            self.request.session.set_expiry(0)

            self.request.session.modified = True


        super(login, self).form_valid(form)


        for v in Vendor.objects.all():
            if(v.username == username):
                return redirect(to='dashboard')


        for c in Customer.objects.all():
            if(c.username == username):
                return redirect(to='customerdashboard')




def customerdashboard(request):

    vendor = ''
    customer = ''

    try:
        vendor = Vendor.objects.get(username=request.user.username)
        return render(request, 'mnotes/vendorpages/dashboard.html', {})
    except ObjectDoesNotExist:
        print('does not exist')

    try:
        customer = Customer.objects.get(username=request.user.username)
        return render(request, 'mnotes/customerpages/customerdashboard.html', {})
    except ObjectDoesNotExist:
        print('does not exist')
      

class signup(View):
    form_class = SignUpForm
    initial = {'key' : 'value'}
    template_name = 'mnotes/vendorpages/signup.html'
    form_class_vendor = VendorForm
    form_class_customer = CustomerForm
    login_form = LoginForm()

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(signup, self).dispatch(request, *args, **kwargs)
   
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        vendor_Form = self.form_class_vendor(initial=self.initial)
        customer_Form = self.form_class_customer(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'vendor_Form' : vendor_Form, 'customer_Form' : customer_Form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        vendor_Form = self.form_class_vendor(request.POST)
        customer_Form = self.form_class_customer(request.POST)
        if request.POST.get('vendor'):
            customer_Form = None
            print(form.errors)
            if form.is_valid() and vendor_Form.is_valid():            
                vendor_name = vendor_Form.cleaned_data.get('vendor_name')
                vendor_email = vendor_Form.cleaned_data.get('vendor_email')
                vendor_tg = vendor_Form.cleaned_data.get('vendor_tg')
                vendor_insta = vendor_Form.cleaned_data.get('vendor_insta')
                vendor_phone_number = vendor_Form.cleaned_data.get('vendor_phone_number')
                store_name = vendor_Form.cleaned_data.get('store_name')
                store_type = vendor_Form.cleaned_data.get('store_type')
                store_website = vendor_Form.cleaned_data.get('store_website')
                date_registered = vendor_Form.cleaned_data.get('date_registered')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                store_address = vendor_Form.cleaned_data.get('store_address')   

                if(username.lower() == username):
                    form.save()
                    Vendor.objects.create(vendor_insta=vendor_insta, store_address=store_address, vendor_name=vendor_name, vendor_email=vendor_email, vendor_tg=vendor_tg, vendor_phone_number=vendor_phone_number, store_name=store_name, store_type=store_type, store_website=store_website, date_registered=date_registered, username=username, password=password)
                    messages.success(request, f'{username} uchun Akkount yaratildi, quyidagi forma orqali akkountingizga kiring.')
                    print("akkount yaratildi")
                    return redirect(to='dashboard')
                else:
                    print("Akkount yaratilmadi")
                    messages.error(request, f'{username} uchun akkount yaratilmadi, nomni faqat kichkina xarflarda kiriting.')
                    return redirect(to='signupselect')

        elif request.POST.get("customer"):
            vendor_Form = None
            print(form.errors)
            if form.is_valid() and customer_Form.is_valid():
                customer_name = customer_Form.cleaned_data.get('customer_name')
                customer_email = customer_Form.cleaned_data.get('customer_email')
                customer_insta = customer_Form.cleaned_data.get('customer_insta')
                customer_phone_number = customer_Form.cleaned_data.get('customer_phone_number')
                customer_tg = customer_Form.cleaned_data.get('customer_tg')
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                date_registered = customer_Form.cleaned_data.get('date_registered')


                if(username.lower() == username):
                    form.save()
                    Customer.objects.create(customer_name=customer_name, customer_email=customer_email, customer_insta=customer_insta, customer_tg=customer_tg, customer_phone_number=customer_phone_number,
                                username=username, password=password, date_registered=date_registered)
                    messages.success(request, f'{username} uchun Akkount yaratildi, quyidagi forma orqali akkountingizga kiring.')
                    print("akkount yaratildi")
                    return redirect(to='login')
                else:                    
                    messages.error(request, f'{username} uchun akkount yaratilmadi, nomni faqat kichkina xarflarda kiriting.')
                    print("akkount yaratilmadi")
                    return redirect(to='signupselect')

        return render(request, self.template_name, {'form' : form, 'vendor_Form' : vendor_Form, 'customer_Form' : customer_Form}) #'vendor_Form' : vendor_Form})


def signupselect(request):

    context = {}
    return render(request, 'mnotes/vendorpages/signupselect.html', context)


class changepassword(SuccessMessageMixin, PasswordChangeView):
    template_name = 'mnotes/change_password.html'
    sucess_message = "Parolni muvaffaqiyatli o'zgartirdingiz"
    success_url = reverse_lazy('index')


@login_required
def soldproducts(request):
    if is_demo_mode():
        soldproducts_list = get_demo_objects_for_model('ProductSold')
    else:
        soldproducts_list = ProductSold.objects.filter(username=request.user)

    context = {'soldproducts_list' : soldproducts_list}
    return render(request, 'mnotes/vendorpages/soldproducts.html', context)

@login_required
def soldproductview(request, id):

    try:
        soldproduct_props = ProductSold.objects.get(pk=id, username=request.user)
        #product = Product.objects.get(product_name=soldproduct_props.product_name, ) 
    except ProductSold.DoesNotExist:
        soldproduct_props = None
        #product = None

       
    context = {'soldproduct_props' : soldproduct_props}
    return render(request, 'mnotes/vendorpages/soldproductview.html', context)

@login_required
def dashboard(request):
    vendor = ''
    customer = ''
    
    if is_demo_mode():
        user_props = get_demo_profile(get_demo_user())
        product_list = get_demo_objects_for_model('Product')
        todays_date = timezone.now()
    else:
        user_props = Profile.objects.get(user=request.user)
        product_list = Product.objects.filter(user=request.user)
        todays_date = timezone.now()
    
    full_product_initial_price = 0

    #All product count
    labels = []
    data = []
    full_product_count = 0
    queryset = product_list
    for count in queryset:
        full_product_count = count.product_count
        labels.append(count.product_name)
        data.append(full_product_count)

    labels3 = []
    data3 = []
    product_sold_budget = 0
    full_budget_product_sold = 0
    
    if is_demo_mode():
        queryset3 = get_demo_objects_for_model('ProductSold').filter(date_sold=todays_date.date())
    else:
        queryset3 = ProductSold.objects.filter(username=request.user, date_sold=todays_date)
        
    for count in queryset3:
        if(count.isfullypaid):
            product_sold_budget += count.product_sold_price * count.product_sold_count
            date = count.date_sold.strftime('%m/%d/%Y')
            labels3.append(date)
            data3.append(product_sold_budget)

            full_budget_product_sold = data3[-1] if data3 else 0


    #Daily profit
    labels2 = []
    data2 = []
    pure_profit = 0
    
    if is_demo_mode():
        product_profits = get_demo_objects_for_model('ProductSold').filter(date_sold=todays_date.date())
    else:
        product_profits = ProductSold.objects.filter(username=request.user, date_sold=todays_date)
        
    full_profit_day = 0
    queryset2 = product_profits
    for pr in queryset2:
        if(pr.isfullypaid):
            pure_profit += pr.profit
            date = pr.date_sold.strftime('%m/%d/%Y')
            labels2.append(date)
            data2.append(pure_profit)        

            full_profit_day = data2[-1] if data2 else 0

            if(len(labels2) == 10) and (len(data2) == 10):
                labels2.shift(date)
                data2.shift(pure_profit)


    store_budget = 0
    for t in product_list:
        store_budget += t.product_price_initial * t.product_count

    if is_demo_mode():
        trade_count = get_demo_objects_for_model('ProductSold').count()
        all_sold_products = get_demo_objects_for_model('ProductSold')
    else:
        trade_count = ProductSold.objects.filter(username=request.user).count()
        all_sold_products = ProductSold.objects.filter(username=request.user)

    trade_budget = 0
    for k in all_sold_products:
        trade_budget += k.product_sold_price * k.product_sold_count


    most_sold_5_products = []
    count_list = []
    sold_count = 0
    #adding 5 elements

    for q in product_list:        
        sold_count = q.sold_count
        if(len(most_sold_5_products) < 3):
            most_sold_5_products.append(q)

        for t in most_sold_5_products:
            if(t.sold_count < q.sold_count and q.sold_count != 0):
                most_sold_5_products.remove(t)
                most_sold_5_products.append(q)


    #discounts
    #print(todays_date) #last_discount_date=todays_date.strftime("%m-%d-%y")
    todays_discount_products = product_list
    todays_2_discount_products = []

    for discount_product in todays_discount_products:
        if(len(todays_2_discount_products) < 2 and discount_product.discount != 0 and discount_product.last_discount_date.strftime("%m-%d-%y") == todays_date.strftime("%m-%d-%y")):
            todays_2_discount_products.append(discount_product)
#            print(discount_product.last_discount_date)
    try:
        if is_demo_mode():
            vendor_obj = get_demo_vendor(get_demo_user().username)
            if vendor_obj:
                vendor = vendor_obj
                vendor_props = vendor_obj
        else:
            vendor = Vendor.objects.get(username=request.user.username)
            vendor_props = Vendor.objects.get(username=request.user)
            
        context = {'todays_2_discount_products' : todays_2_discount_products, 'most_sold_5_products': most_sold_5_products,'trade_budget': trade_budget, 'trade_count': trade_count, 'store_budget': store_budget, 'vendor_props' : vendor_props, 'user_props' : user_props, 'full_budget_product_sold': full_budget_product_sold, 'full_profit_day': full_profit_day, 'pure_profit':pure_profit, 'labels3' : labels3, 'data3' : data3, 'labels': labels, 'data': data, 'labels2' : labels2, 'data2' : data2}

        return render(request, 'mnotes/vendorpages/dashboard.html', context)
    except (ObjectDoesNotExist, AttributeError):
        pass
#        print('does not exist')

    try:
        if not is_demo_mode():
            customer = Customer.objects.get(username=request.user.username)
        return render(request, 'mnotes/customerpages/customerdashboard.html', {})
    except ObjectDoesNotExist:
	    pass
#        print('does not exist')


def creatediscount(request, id):
    product = Product.objects.get(pk=id)

    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():

            discount = form.cleaned_data.get('discount')
            product.last_discount_date = timezone.now()
            product.discount_in_sum = ( product.product_price_told * discount ) / 100

            product.save()
            messages.success(request, 'Chegirma muvaffaqiyatli yaratildi')

            form.save()
            url = "../viewdiscounts/"
            return redirect('dashboard')

    else:
        form = ProductForm(instance=product)

    context = {'product' : product}
    return render(request, 'mnotes/vendorpages/creatediscount.html', context)

def creatediscountselect(request):
    product_list = Product.objects.filter(user=request.user)
    context = { 'product_list' : product_list }
    return render(request, 'mnotes/vendorpages/creatediscountselect.html', context)

def viewdiscounts(request):
    product_list = Product.objects.filter(user=request.user)

    discounted_product_list = []

    for i in product_list:
        if(i.discount != 0):
            discounted_product_list.insert(0, i)


    for k in discounted_product_list:
        print(k.last_discount_date)
    context = {'discounted_product_list': discounted_product_list, 'product_list' : product_list}
    return render(request, 'mnotes/vendorpages/viewdiscounts.html', context)

def reports(request):

    context = {}
    return render(request, 'mnotes/vendorpages/reports.html', context)


def customerdashboard(request):
    try:
        vendor = Vendor.objects.get(username=request.user.username)
        vendor_props = Vendor.objects.get(username=request.user)    
        context = {}

        return render(request, 'mnotes/vendorpages/Error.html', context)
    except ObjectDoesNotExist:
        print('does not exist')

    try:
        customer = Customer.objects.get(username=request.user.username)
        return render(request, 'mnotes/customerpages/customerdashboard.html', {})
    except ObjectDoesNotExist:
        print('does not exist')

def customerprofile(request):
    user = Customer.objects.get(username=request.user.username)
    context = {'user' : user}

    return render(request, 'mnotes/customerpages/profile.html', context)

def vendors(request):

    context = {}

    return render(request, 'mnotes/customerpages/vendors.html', context)
    
def view_vendor(request, vendor_id):

    vendor = Vendor.objects.get(pk=vendor_id)

    context = {'vendor' : vendor}
    return render(request, 'mnotes/customerpages/view_vendor.html', context)

def customercontact(request):

    context = {}
    return render(request, 'mnotes/customerpages/customercontact.html', context)
