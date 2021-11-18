from django.forms import ModelForm
from django.db import models
from django.views.generic import UpdateView
from .models import Notes, Product, Profile, ProductSold, SellOnDebt, BuyOnDebt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone
from django import forms
from multiselectfield import MultiSelectField
from django.utils.translation import gettext_lazy as _
class UpdateUserForm(ModelForm):
    username = forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']


class UpdateProfileForm(ModelForm):
    bio = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['bio', 'image']

class SignUpForm(UserCreationForm):
    error_messages = {
        'password_mismatch': 'Ikki xil parol kiritildi',
        'unique':'Bu nom bilan akkount mavjud, boshqa nom tanlang',
    }
    username = forms.CharField(error_messages=error_messages, max_length=15, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nom', 'class': 'form-control'}))
    password1 = forms.CharField(error_messages=error_messages, max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Parol', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password' }))
    password2 = forms.CharField(error_messages=error_messages, max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Parolni takrorlang', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password'}))
    class Meta:
        
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Nom', 'class': 'form-control', }))
    password = forms.CharField(max_length=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Parol', 'class': 'form-control', 'data-toggle': 'password', 'id': 'password', 'name': 'password', }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']

class NotesForm(forms.ModelForm):
    nametest = forms.CharField(label='nametest', max_length=100)
    class Meta:
        model = Notes
        fields = ('__all__')

class ProductForm(forms.ModelForm):
    isdebt = forms.BooleanField(required=False)
    product_price_initial = forms.IntegerField(required=False)
    product_price_told = forms.IntegerField(required=False)

    class Meta:
        model = Product
        fields = ('__all__')
        exclude = ('user', 'datetime')
        widgets = {
            'product_name' : forms.TextInput(attrs={'placeholder': 'Nom', 'class': 'form-control', }),
            'product_price_initial' : forms.NumberInput(attrs={'placeholder': 'Kelgan narx', 'class': 'form-control', }),
            'product_price_told' : forms.NumberInput(attrs={'placeholder': 'Aytilar narx', 'class' : 'form-control', }),
            'product_price_told' : forms.NumberInput(attrs={'placeholder': 'Aytilar narx', 'class' : 'form-control', }),
            'product_count' : forms.NumberInput(attrs={'placeholder': 'Son', 'class': 'form-control', }),
        }
        labels = {
            'product_name' : _('product_name'),
            'product_price_initial' : _('product_price_initial'),
            'product_price_told' : _('product_price_told'),
            'product_count' : _('product_count'),
            'isdebt' : _('isdebt'),
        }
      
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        # add custom error messages
        self.fields['product_name'].error_messages.update({
            'required': 'Mahsulot nomini kiritmadingiz!',
        })
        self.fields['product_price_initial'].error_messages.update({
            'required': 'Mahsulot tan narxini kiritmadingiz!',
        })        
        self.fields['product_price_told'].error_messages.update({
            'required': 'Mahsulot aytilish kiritmadingiz!',
        })
        self.fields['product_count'].error_messages.update({
            'required': 'Mahsulot sonini kiritmadingiz!',
        })
class ProductSoldForm(forms.ModelForm):
    isdebt = forms.BooleanField(required=False)

    class Meta:
        model = ProductSold
        fields = ['product_sold_price','product_sold_count']
        exclude = ('user', 'given_date', 'product_name')
        widgets = {
            'product_sold_price' : forms.NumberInput(attrs={'placeholder' : 'Sotilgan mahsulot narxi', 'class' : 'form-control'}),
            'product_sold_count' : forms.NumberInput(attrs={'placeholder' : 'Sotilgan mahsulot soni', 'class' : 'form-control'}),
        }
        labels = {
            'product_sold_price' : _('product_sold_price'),
            'product_sold_count' : _('product_sold_count'),
            'isdebt' : _('isdebt'),
        }


class SellOnDebtForm(forms.ModelForm):
    due_date = forms.DateField(required=False)
    product_name = forms.CharField(max_length=200, required=False)
    product_count = forms.IntegerField(required=False)
    product_price = forms.IntegerField(required=False)
    customer_name = forms.CharField(required=False)
    customer_phone = forms.IntegerField(required=False)
    isfullypaid = forms.BooleanField(required=False)
    ispartlypaid = forms.BooleanField(required=False)
    paid_amount = forms.IntegerField(required=False)
    left_amount = forms.IntegerField(required=False)

    class Meta:
        model = SellOnDebt
        fields = ('__all__')
        exclude = ('user', 'given_date')

        widgets = {
            'product_name' : forms.TextInput(attrs={'placeholder' : 'Mahsulot nomi', 'class' : 'form-control'}),
            'product_price' : forms.NumberInput(attrs={'placeholder' : 'Mahsulot narxi', 'class' : 'form-control'}),
            'customer_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'customer_phone' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }

        labels = {
            'product_name' : _('product_name'),
            'product_price' : _('product_price'),
            'customer_name' : _('customer_name'),
            'customer_phone' : _('customer_phone'),
            'due_date' : _('due_date'),
                'paid_amount' : _('paid_amount'),
            'left_amount' : _('left_amount'),
        }

class BuyOnDebtForm(forms.ModelForm):
    due_date = forms.DateField(required=False)
    product_name = forms.CharField(max_length=200, required=False)
    product_count = forms.IntegerField(required=False)
    product_price = forms.IntegerField(required=False)
    isfullypaid = forms.BooleanField(required=False)
    ispartlypaid = forms.BooleanField(required=False)
    paid_amount = forms.IntegerField(required=False)
    left_amount = forms.IntegerField(required=False)

    class Meta:
        model = BuyOnDebt
        fields = ['owner_name', 'owner_phone', 'due_date']
        exclude = ('user', 'given_date')

        widgets = {
            'product_name' : forms.TextInput(attrs={'placeholder' : 'Mahsulot nomi', 'class' : 'form-control'}),
            'product_price' : forms.NumberInput(attrs={'placeholder' : 'Mahsulot narxi', 'class' : 'form-control'}),
            'owner_name' : forms.TextInput(attrs={'class' : 'form-control'}),
            'owner_phone' : forms.NumberInput(attrs={'class' : 'form-control'}),
        }

        labels = {
            'product_name' : _('product_name'),
            'product_price' : _('product_price'),
            'owner_name' : _('owner_name'),
            'owner_phone' : _('owner_phone'),
            'due_date' : _('due_date'),
            'isfullypaid' : _('isfullypaid'),
            'ispartlypaid' : _('ispartlypaid'),
            'paid_amount' : _('paid_amount'),
            'left_amount' : _('left_amount'),
        }