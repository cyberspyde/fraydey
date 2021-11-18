from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .forms import SellOnDebtForm, BuyOnDebtForm, ProductSoldForm, NotesForm, ProductForm, SignUpForm, LoginForm, UpdateProfileForm, UpdateUserForm
from .models import Notes, Product, ProductSold, Profile, SellOnDebt, BuyOnDebt, User
from django.db.models import Q
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
import socketserver, json
from wsgiref import handlers
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
    context = {'product_list' : product_list}
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


                BuyOnDebt.objects.create(user=product.user, product_name=product_name, product_count=product_count, product_price=product_price_initial, owner_name=owner_name, owner_phone=owner_phone, due_date=due_date, paid_amount=paid_amount, left_amount=left_amount, isfullypaid=isfullypaid, ispartlypaid=ispartlypaid)

            messages.success(request, 'Mahsulot muvaffaqiyatli yaratildi')
            return redirect('/inventory/')
        else:
            print ("Form is not valid")
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
    selldebt_props = SellOnDebt.objects.filter(user=request.user, pk=id)

    context = {'selldebt_props' : selldebt_props }
    return render(request, 'mnotes/selldebtview.html', context)

def buydebtview(request, id):
    buydebt_props = BuyOnDebt.objects.filter(user=request.user, pk=id)

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
        searched = request.POST['searched']
        products = Product.objects.filter(product_name__contains=searched, user=request.user)
    else:
        searched = ""
        products = ""
    context = { 'searched' : searched, 'products' : products}
    return render(request, 'mnotes/searchsoldproduct.html', context)

def searchbuydebt(request):
    if request.method == 'POST':
        searchedbuydebt = request.POST['searchedbuydebt']
        buydebt = BuyOnDebt.objects.filter( Q(product_name__contains=searchedbuydebt, user=request.user) | Q(owner_name__contains=searchedbuydebt, user=request.user))
        buydebt_list = BuyOnDebt.objects.filter(user=request.user)
    else:
        searchedbuydebt = ""
        buydebt = ""
        buydebt_list = ""

    context = {'searchedbuydebt' : searchedbuydebt, 'buydebt' : buydebt, 'buydebt_list' : buydebt_list}
    return render(request, 'mnotes/searchbuydebt.html', context)

def searchbuydebtselect(request):
    if request.method == 'POST':
        searchedbuydebtselect = request.POST['searchedbuydebtselect']
        buydebt = Product.objects.filter(product_name__contains=searchedbuydebtselect, user=request.user)
    else:
        searchedbuydebtselect = ""
        buydebt = ""
    context = { 'searchedbuydebtselect' : searchedbuydebtselect, 'buydebt' : buydebt}
    return render(request, 'mnotes/searchbuydebtselect.html', context)

def searchselldebt(request):
    if request.method == 'POST':
        searchedselldebt = request.POST['searchedselldebt']
        selldebt = SellOnDebt.objects.filter( Q(product_name__contains=searchedselldebt, user=request.user) | Q(customer_name__contains=searchedselldebt, user=request.user))
        selldebt_list = SellOnDebt.objects.filter(user=request.user)
    else:
        searchedselldebt = ""
        selldebt = ""
        selldebt_list = ""

    context = {'searchedselldebt' : searchedselldebt, 'selldebt' : selldebt, 'selldebt_list' : selldebt_list}
    return render(request, 'mnotes/searchselldebt.html', context)

def searchselldebtselect(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        selldebt = Product.objects.filter(product_name__contains=searched, user=request.user)
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

                

                ProductSold.objects.create(product_sold_price=sold_price, product_sold_count=sold_count, product_sold_id=id, profit=profit, isdebt=isdebt)
 
                if(isdebt):
                    SellOnDebt.objects.create(user=request.user, product_name=product.product_name, product_price=product.product_price_initial, product_count=sold_count, customer_name=customer_name, customer_phone=customer_phone, due_date=due_date, isfullypaid=isfullypaid, ispartlypaid=ispartlypaid, paid_amount=paid_amount, left_amount=left_amount)
               
                messages.success(request, 'Sotilgan mahsulot muvaffaqiyatli saqlandi.')

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
    sellondebt_list = SellOnDebt.objects.filter(user=request.user)
    buyondebt_list = BuyOnDebt.objects.filter(user=request.user)
    product_list = Product.objects.filter(user=request.user)


    context = {'sellondebt_list' : sellondebt_list, 'buyondebt_list' : buyondebt_list, 'product_list' : product_list}
    return render(request, 'mnotes/debts.html', context)


def givedebt(request, id):
    
    if request.method == 'POST':
        form = SellOnDebtForm()
        if form.is_valid():
            messages.success(request, 'Qarzga berilgan mahsulot muvaffaqiyatli saqlandi.')
            redirect('debts')
    else:
        form = SellOnDebtForm()
    context = {'form' : form}
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
        print('errors')
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
            BuyOnDebt.objects.create(user=request.user, product_name=product.product_name, product_count=product_count, product_price=product_price, paid_amount=paid_amount, left_amount=left_amount, ispartlypaid=ispartlypaid, isfullypaid=isfullypaid, due_date=due_date, owner_name=owner_name, owner_phone=owner_phone)
            messages.success(request, 'Qarzga olingan mahsulot muvaffaqiyatli saqlandi.')
            redirect('debts')

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
    user = request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Akkountingiz muvaffaqiyatli yangilandi')
            #return render(request, 'mnotes/profile.html', {'user_form' : user_form, 'profile_form' : profile_form, 'img_obj': img_obj})
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    profile = Profile.objects.filter(user=request.user)


    return render(request, 'mnotes/profile.html', {'user' : user, 'user_form' : user_form, 'profile_form' : profile_form, 'profile' : profile})

def editprofile(request, username):
    user = request.user
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Akkountingiz muvaffaqiyatli yangilandi')
            #return render(request, 'mnotes/profile.html', {'user_form' : user_form, 'profile_form' : profile_form, 'img_obj': img_obj})
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    
    profile = Profile.objects.filter(user=request.user)
    context = {'user' : user, 'user_form' : user_form, 'profile_form' : profile_form, 'profile' : profile}
    return render(request, 'mnotes/editprofile.html', context)



class login(LoginView):
    form = LoginForm()

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:

            self.request.session.set_expiry(0)

            self.request.session.modified = True

        return super(login, self).form_valid(form)


class signup(View):
    form_class = SignUpForm
    initial = {'key' : 'value'}
    template_name = 'mnotes/signup.html'
    
    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(signup, self).dispatch(request, *args, **kwargs)
   
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username} uchun Akkount yaratildi')
            return redirect(to='login')

        return render(request, self.template_name, {'form' : form})

class changepassword(SuccessMessageMixin, PasswordChangeView):
    template_name = 'mnotes/change_password.html'
    sucess_message = "Parolni muvaffaqiyatli o'zgartirdingiz"
    success_url = reverse_lazy('index')
