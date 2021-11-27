from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import  VendorForm, SellOnDebtForm, BuyOnDebtForm, ProductSoldForm, NotesForm, ProductForm, SignUpForm, LoginForm, UpdateProfileForm, UpdateUserForm
from .models import  Vendor, Notes, Product, ProductSold, Profile, SellOnDebt, BuyOnDebt, User
from django.db.models import Q
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
import socketserver, json
from wsgiref import handlers
from datetime import date, timedelta
import datetime
from django.utils import timezone
socketserver.BaseServer.handle_error = lambda *args, **kwargs: None
handlers.BaseHandler.log_exception = lambda *args, **kwargs: None
# Create your views here.


def index(request):


    return render(request, 'mnotes/index.html')

def takenoteview(request):
    return HttpResponse("Entered text : " + str(request.POST.get('nametest')))

@login_required
def savednotes(request):
    notes_list = Notes.objects.filter(user=request.user)

    return render(request, 'mnotes/savednotes.html', {'notes_list' : notes_list} )

@login_required
def inventory(request):
    product_list = Product.objects.filter(user=request.user)
    username = User.objects.get(pk=request.user.id)
    context = {'product_list' : product_list, 'user_name' : username}
    return render(request, 'mnotes/inventory.html', context)

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


                BuyOnDebt.objects.create(username=product.user, product_name=product_name, product_count=product_count, product_price=product_price_initial, owner_name=owner_name, owner_phone=owner_phone, due_date=due_date, paid_amount=paid_amount, left_amount=left_amount, isfullypaid=isfullypaid, ispartlypaid=ispartlypaid)

            messages.success(request, 'Mahsulot muvaffaqiyatli yaratildi')
            return redirect('/inventory/')
    else:
        form = ProductForm()
        BuyDebtForm = BuyOnDebtForm()
    context = {'form' : form, 'BuyDebtForm' : BuyDebtForm}
    return render(request, 'mnotes/createproduct.html', context)

def productview(request, id):
    product_props = Product.objects.filter(user=request.user, pk=id)
    
    context = {'product_props' : product_props}
    return render(request, 'mnotes/productview.html', context)

def selldebtview(request, id):
    selldebt_props = SellOnDebt.objects.get(username=request.user, pk=id)

    context = {'selldebt_props' : selldebt_props }
    return render(request, 'mnotes/selldebtview.html', context)

def buydebtview(request, id):
    buydebt_props = BuyOnDebt.objects.filter(username=request.user, pk=id)

    context = {'buydebt_props' : buydebt_props }
    return render(request, 'mnotes/buydebtview.html', context)

def searchfunction(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        products = Product.objects.filter(product_name__contains=searched, user=request.user)
    else:
        searched = ""
        products = ""
    context = { 'searched' : searched, 'products' : products}
    return render(request, 'mnotes/searchfunction.html', context)

def searchsoldproduct(request):
    if request.method == 'POST':
        searched = request.POST['searchedsoldproduct']
        products = ProductSold.objects.filter(product_name__contains=searched, username=request.user)
        debtproducts = SellOnDebt.objects.filter(product_name__contains=searched, username=request.user)
    else:
        searched = ""
        products = ""
        debtproducts = ""
    context = { 'searched' : searched, 'products' : products, 'debtproducts' : debtproducts}
    return render(request, 'mnotes/searchsoldproduct.html', context)

def searchsoldproductone(request):
    if request.method == 'POST':
        searched = request.POST['searchedsoldproductone']
        products = Product.objects.filter(product_name__contains=searched, user=request.user)
    else:
        searched = ""
        products = ""
    context = { 'searched' : searched, 'products' : products}
    return render(request, 'mnotes/searchsoldproductone.html', context)

def searchbuydebt(request):
    if request.method == 'POST':
        searchedbuydebt = request.POST['searchedbuydebt']
        buydebt = BuyOnDebt.objects.filter( Q(product_name__contains=searchedbuydebt, username=request.user) | Q(owner_name__contains=searchedbuydebt, username=request.user))
        buydebt_list = BuyOnDebt.objects.filter(username=request.user)
    else:
        searchedbuydebt = ""
        buydebt = ""
        buydebt_list = ""

    context = {'searchedbuydebt' : searchedbuydebt, 'buydebt' : buydebt, 'buydebt_list' : buydebt_list}
    return render(request, 'mnotes/searchbuydebt.html', context)

def searchbuydebtselect(request):
    if request.method == 'POST':
        searchedbuydebtselect = request.POST['searchedbuydebtselect']
        buydebt = Product.objects.filter(product_name__contains=searchedbuydebtselect, username=request.user)
    else:
        searchedbuydebtselect = ""
        buydebt = ""
    context = { 'searchedbuydebtselect' : searchedbuydebtselect, 'buydebt' : buydebt}
    return render(request, 'mnotes/searchbuydebtselect.html', context)

def searchselldebt(request):
    if request.method == 'POST':
        searchedselldebt = request.POST['searchedselldebt']
        selldebt = SellOnDebt.objects.filter( Q(product_name__contains=searchedselldebt, username=request.user) | Q(customer_name__contains=searchedselldebt, username=request.user))
        selldebt_list = SellOnDebt.objects.filter(username=request.user)
    else:
        searchedselldebt = ""
        selldebt = ""
        selldebt_list = ""

    context = {'searchedselldebt' : searchedselldebt, 'selldebt' : selldebt, 'selldebt_list' : selldebt_list}
    return render(request, 'mnotes/searchselldebt.html', context)

def searchselldebtselect(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        selldebt = Product.objects.filter(product_name__contains=searched, username=request.user)
    else:
        searched = ""
        selldebt = ""
    context = { 'searched' : searched, 'selldebt' : selldebt}
    return render(request, 'mnotes/searchselldebtselect.html', context)

def sellproduct(request):
    product_list = Product.objects.filter(user=request.user)
    
    context = { 'product_list' : product_list }
    return render(request, 'mnotes/sellproduct.html', context)

def deleteproduct(request, id):

    product = Product.objects.get(pk=id)
    product.delete()
    messages.success(request, 'Mahsulot muvaffaqiyatli o`chirildi')
    return redirect('inventory')

def productsold(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        SoldProductForm = ProductSoldForm(request.POST)
        SellDebtForm = SellOnDebtForm(request.POST)

        if SoldProductForm.is_valid() and SellDebtForm.is_valid():

            sold_price = SoldProductForm.cleaned_data.get('product_sold_price')
            sold_count = SoldProductForm.cleaned_data.get('product_sold_count')
            isdebt = SoldProductForm.cleaned_data.get('isdebt')
            user = request.user

            product_name = Product.objects.get(pk=id).product_name
            customer_name = SellDebtForm.cleaned_data.get('customer_name')
            customer_phone = SellDebtForm.cleaned_data.get('customer_phone')
            due_date = SellDebtForm.cleaned_data.get('due_date')
            isfullypaid = SellDebtForm.cleaned_data.get('isfullypaid')
            ispartlypaid = SellDebtForm.cleaned_data.get('ispartlypaid')
            paid_amount = SellDebtForm.cleaned_data.get('paid_amount')
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
               
                product.save()

                profit = (sold_price - initial_price)*sold_count

                

                ProductSold.objects.create(product_name=product_name, username=request.user, product_sold_price=sold_price, product_sold_count=sold_count, product_sold_id=id, profit=profit, isdebt=isdebt)
                    
                if(isdebt):
                    SellOnDebt.objects.create(username=request.user, product_name=product.product_name, product_price=product.product_price_initial, 
                        product_count=sold_count, customer_name=customer_name, customer_phone=customer_phone, due_date=due_date, isfullypaid=isfullypaid, 
                        ispartlypaid=ispartlypaid, paid_amount=paid_amount, left_amount=left_amount, profit=profit)
                
                messages.success(request, 'Sotilgan mahsulot muvaffaqiyatli saqlandi.')
                return redirect('inventory')
        else:
            
            profit = 0
    else:
        SoldProductForm = ProductSoldForm() 
        SellDebtForm = SellOnDebtForm()  
        profit = 0

    sold_product_list = ProductSold.objects.filter(product_sold_id=id)
    total_profit = 0
    for value in sold_product_list:
        
        total_profit += value.profit

    
    context = {'product' : product, 'SoldProductForm' : SoldProductForm, 'profit' : profit, 'SellDebtForm' : SellDebtForm}    
    return render(request, 'mnotes/productsold.html', context)

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
    return render(request, 'mnotes/editproduct.html', context)

def sales(request):
    return render(request, 'mnotes/sales.html', {})


@login_required
def debts(request):
    sellondebt_list = SellOnDebt.objects.filter(username=request.user)
    buyondebt_list = BuyOnDebt.objects.filter(username=request.user)
    product_list = Product.objects.filter(user=request.user)


    context = {'sellondebt_list' : sellondebt_list, 'buyondebt_list' : buyondebt_list, 'product_list' : product_list}
    return render(request, 'mnotes/debts.html', context)


def givedebt(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = SellOnDebtForm(request.POST)

        if form.is_valid():
            product_name = product.product_name
            product_count = form.cleaned_data.get('product_count')
            product_price = form.cleaned_data.get('product_price')
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
                left_amount = product_count * product_price - paid_amount


            if(product_count > product.product_count):
                messages.warning(request, 'Sizda bu miqdorda mahsulot mavjud emas!')
                profit = 0
            else:
                isfullypaid = False
                
                #updating the product's count and isdebt values in the database
                final_product_count = product.product_count + product_count
                product.product_count = final_product_count
                product.isdebt = True
                product.save()

                profit = (product_price - product.product_price_initial)*product_count



            SellOnDebt.objects.create(username=request.user, product_name=product_name, product_count=product_count, product_price=product_price,
                                        customer_name=customer_name, customer_phone=customer_phone, due_date=due_date, paid_amount=paid_amount, 
                                        left_amount=left_amount, ispartlypaid=ispartlypaid, isfullypaid=isfullypaid, profit=profit)
            messages.success(request, 'Qarzga berilgan mahsulot muvaffaqiyatli saqlandi.')
            return redirect('debts')
    else:

        form = SellOnDebtForm()
    context = {'product' : product, 'form' : form}
    return render(request, 'mnotes/givedebt.html', context)


def givedebtselect(request):
    product_list = Product.objects.filter(user=request.user)
    
    context = { 'product_list' : product_list }
    return render(request, 'mnotes/givedebtselect.html', context)



def returndebt(request, id):
    debt = SellOnDebt.objects.get(pk=id)
    if request.method == 'POST':
        debt.isfullypaid = True
        debt.save()
        redirect('debts')
    else:
        redirect('debts')
    return redirect('debts')


def paydebt(request, id):
    debt = BuyOnDebt.objects.get(pk=id)
    if request.method == 'POST':
        debt.isfullypaid = True
        debt.save()
        messages.success(request, 'Qarz muvaffaqiyatli to`landi')
        redirect('debts')
    else:
        redirect('debts')
    return redirect('debts')

def getdebt(request, id):
    product = Product.objects.get(pk=id)
    if request.method == 'POST':
        form = BuyOnDebtForm(request.POST)
        if form.is_valid():
            paid_amount = form.cleaned_data.get('paid_amount')
            product_count = form.cleaned_data.get('product_count')
            product_price = form.cleaned_data.get('product_price')
            ispartlypaid = form.cleaned_data.get('ispartlypaid')
            due_date = form.cleaned_data.get('due_date')
            owner_name = form.cleaned_data.get('owner_name')
            owner_phone = form.cleaned_data.get('owner_phone')
            isfullypaid = False

            #updating the product's count and isdebt values in the database
            final_product_count = product.product_count + product_count
            product.product_count = final_product_count
            product.isdebt = True
            product.save()

            if(paid_amount is None):
                paid_amount = 0
                left_amount = 0
            else:
                left_amount = product_count * product_price - paid_amount
            BuyOnDebt.objects.create(username=request.user, product_name=product.product_name, product_count=product_count, product_price=product_price, paid_amount=paid_amount, left_amount=left_amount, ispartlypaid=ispartlypaid, isfullypaid=isfullypaid, due_date=due_date, owner_name=owner_name, owner_phone=owner_phone)
            
            messages.success(request, 'Qarzga olingan mahsulot muvaffaqiyatli saqlandi.')
            return redirect('debts')

    else:
        form = BuyOnDebtForm()

    context = {'form' : form, 'product' : product}
    return render(request, 'mnotes/getdebt.html', context)


def getdebtselect(request):
    product_list = Product.objects.filter(user=request.user)
    
    context = { 'product_list' : product_list }
    return render(request, 'mnotes/getdebtselect.html', context)

@login_required
def profile(request):
    user_props = Profile.objects.get(user=request.user)
    vendor_props = Vendor.objects.get(username=request.user)

    return render(request, 'mnotes/profile.html', {'user_props' : user_props, 'vendor_props' : vendor_props})


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
    return render(request, 'mnotes/editprofile.html', context)



class login(LoginView):
    form = LoginForm()

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:

            self.request.session.set_expiry(0)

            self.request.session.modified = True

        super(login, self).form_valid(form)

        return redirect(to='inventory')

        

class signup(View):
    form_class = SignUpForm
    initial = {'key' : 'value'}
    template_name = 'mnotes/signup.html'
    form_class_vendor = VendorForm
    
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(signup, self).dispatch(request, *args, **kwargs)
   
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        vendor_Form = self.form_class_vendor(initial=self.initial)
        return render(request, self.template_name, {'form': form, 'vendor_Form' : vendor_Form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        vendor_Form = self.form_class_vendor(request.POST)
        
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

            form.save()
            Vendor.objects.create(vendor_insta=vendor_insta, store_address=store_address, vendor_name=vendor_name, vendor_email=vendor_email, vendor_tg=vendor_tg, vendor_phone_number=vendor_phone_number, store_name=store_name, store_type=store_type, store_website=store_website, date_registered=date_registered, username=username, password=password)
            messages.success(request, f'{username} uchun Akkount yaratildi')
            return redirect(to='login')
            
        return render(request, self.template_name, {'form' : form}) #'vendor_Form' : vendor_Form})





class changepassword(SuccessMessageMixin, PasswordChangeView):
    template_name = 'mnotes/change_password.html'
    sucess_message = "Parolni muvaffaqiyatli o'zgartirdingiz"
    success_url = reverse_lazy('index')


@login_required
def soldproducts(request):
    soldproducts_list = ProductSold.objects.filter(username=request.user)
    soldondebtproducts_list = SellOnDebt.objects.filter(username=request.user)


    context = {'soldproducts_list' : soldproducts_list, 'soldondebtproducts_list' : soldondebtproducts_list}
    return render(request, 'mnotes/soldproducts.html', context)

@login_required
def soldproductview(request, id):

    try:
        soldproduct_props = ProductSold.objects.get(pk=id, username=request.user)
    except ProductSold.DoesNotExist:
        soldproduct_props = None

    try: 
        soldondebtproduct_props = SellOnDebt.objects.get(pk=id, username=request.user)
    except SellOnDebt.DoesNotExist:
        soldondebtproduct_props = None

    context = {'soldproduct_props' : soldproduct_props, 'soldondebtproduct_props' : soldondebtproduct_props }
    return render(request, 'mnotes/soldproductview.html', context)


@login_required
def analytics(request):
    product_list = Product.objects.filter(user=request.user)
    full_product_initial_price = 0
    todays_date = timezone.now()

    #All product count
    labels = []
    data = []
    full_product_count = 0
    queryset = product_list
    for count in queryset:
        full_product_count = count.product_count
        labels.append(count.product_name)
        data.append(full_product_count)

    #ProductSold Chart

    labels3 = []
    data3 = []
    product_sold_budget = 0
    full_budget_product_sold = 0
    queryset3 = ProductSold.objects.filter(username=request.user, date_sold=todays_date)
    for count in queryset3:
        product_sold_budget += count.product_sold_price * count.product_sold_count
        date = count.date_sold.strftime('%m/%d/%Y')
        labels3.append(date)
        data3.append(product_sold_budget)

        full_budget_product_sold = data3[-1]


    #Daily profit
    labels2 = []
    data2 = []
    pure_profit = 0
    product_profits = ProductSold.objects.filter(username=request.user, date_sold=todays_date)
    full_profit_day = 0
    queryset2 = product_profits
    for pr in queryset2:
        pure_profit += pr.profit
        date = pr.date_sold.strftime('%m/%d/%Y')
        labels2.append(date)
        data2.append(pure_profit)        
    
        full_profit_day = data2[-1]

        if(len(labels2) == 10) and (len(data2) == 10):
            labels2.shift(date)
            data2.shift(pure_profit)




        
    
    context = {'full_budget_product_sold': full_budget_product_sold, 'full_profit_day': full_profit_day, 'pure_profit':pure_profit, 'labels3' : labels3, 'data3' : data3, 'labels': labels, 'data': data, 'labels2' : labels2, 'data2' : data2}
    return render(request, 'mnotes/analytics.html', context)


 