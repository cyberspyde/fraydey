from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils import timezone
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from multiselectfield import MultiSelectField
from django_resized import ResizedImageField
from django import forms

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    image = ResizedImageField( upload_to='images', size=[300, 400], blank=True, null=True)
    def __str__(self):
        return self.user.username


class Notes(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        output = str(self.pub_date)
        return output


class Product(models.Model):       
    Red = 'Qizil'
    Green = 'Yashil'
    Black = 'Qora'
    Blue = 'Ko`k'
    White = 'Oq'

    M = 'M'
    L = 'L'
    XL = 'XL'
    XXL = 'XXL'
    XXXL = 'XXXL'

    SIZES = (
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL')
    )

    Winter = 'Qishki'
    Summer = 'Yozgi'
    Fall = 'Kuzgi'
    Spring = 'Bahorgi'
    FandS = 'Kuzgi va bahorgi'

    SEASONS = [
        ('Winter', 'Qishki'),
        ('Summer', 'Yozgi'),
        ('Fall', 'Kuzgi'),
        ('Spring', 'Bahorgi'),
        ('FandS', 'Kuzgi va bahorgi')
    ]

    COLORS = [
        ('Qizil', 'Qizil'),
        ('Yashil', 'Yashil'),
        ('Qora', 'Qora'),
        ('Ko`k', 'Ko`k'),
        ('Oq', 'Oq'),
        ('Jigarrang', 'Jigarrang'),
        ('Pushti', 'Pushti'),
        ('Kulrang', 'Kulrang'),
        ('Sariq', 'Sariq')
    ]
    OPTIONS = (
        ("AUT", "Austria"),
        ("DEU", "Germany"),
        ("NLD", "Neitherlands"),
    )


    user = models.OneToOneField(User, on_delete=models.CASCADE)
    product_name = models.CharField(default="Mahsulot nomi", max_length=200)
    product_price_initial = models.IntegerField(default=0)
    product_price_told = models.IntegerField(default=0)
    product_count = models.IntegerField(default=0)
    product_size = MultiSelectField(choices=SIZES, blank=True, null=True)
    product_season = MultiSelectField(choices=SEASONS, blank=True, null=True)
    product_color = MultiSelectField(choices=COLORS, blank=True, null=True)
    product_img = ResizedImageField( upload_to='images', size=[300, 400], blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isdebt = models.BooleanField(default=False)

    def __str__(self):
        output = str(self.user)
        return output

    def save(self, *args, **kwargs):
        super().save()

class ProductSold(models.Model):
    product_sold_price = models.IntegerField()
    product_sold_count = models.IntegerField()
    product_sold_id = models.IntegerField(default=0)
    product_name = models.CharField(max_length=200, default='')
    profit = models.IntegerField(default=0)
    isdebt = models.BooleanField(default=False)
    isfullypaid = models.BooleanField(default=True)
    ispartlypaid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(default=0)
    left_amount = models.IntegerField(default=0)
    username = models.CharField(max_length=200, default='')
    date_sold = models.DateField(auto_now_add=True, editable=False)

    def save(self, *args, **kwargs):
        super().save()

class SellOnDebt(models.Model):
    product_name = models.CharField(max_length=200)
    product_price = models.IntegerField()
    product_count = models.IntegerField()
    customer_phone = models.IntegerField(blank=True, null=True)
    customer_name = models.CharField(max_length=200)
    given_date = models.DateField(auto_now_add=True, editable=False)
    due_date = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=200, default='')
    isfullypaid = models.BooleanField(default=True)
    ispartlypaid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(default=0)
    left_amount = models.IntegerField(default=0)
    profit = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        super().save()

class BuyOnDebt(models.Model):
    product_name = models.CharField(max_length=200)
    product_count = models.IntegerField(default=0)
    product_price = models.IntegerField(default=0)
    owner_name = models.CharField(max_length=200)
    owner_phone = models.IntegerField(default=0)
    date_bought = models.DateField(auto_now_add=True, editable=False)
    due_date = models.DateField(null=True, blank=True)
    username = models.CharField(max_length=200, default='')
    isfullypaid = models.BooleanField(default=False)
    ispartlypaid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(default=0)
    left_amount = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save()

class Vendor(models.Model):
    STORES = [
        ('Kiyimlar', 'Kiyimlar'),
        ('Oyoq kiyim', 'Oyoq kiyim'),
        ('Oziq ovqat', 'Oziq ovqat'),
        ('Mebel', 'Mebel'),
        ('Zargarlik', 'Zargarlik'),
        ('Kosmetika', 'Kosmetika'),
        ('Kanseleriya buyumlari', 'Kanseleriya buyumlari'),
        ('Ichki kiyimlar', 'Ichki kiyimlar'),
        ('Boshqa', 'Boshqa'),
    ]

    vendor_name = models.CharField(max_length=200)
    vendor_email = models.CharField(max_length=200)
    vendor_tg = models.CharField(max_length=200)
    vendor_insta = models.CharField(max_length=200, default='')
    vendor_phone_number = models.IntegerField(null=True, blank=True)
    store_name = models.CharField(max_length=200)
    store_type = models.CharField(max_length=30, choices=STORES, blank=True, null=True)
    store_website = models.CharField(max_length=200)
    store_address = models.CharField(max_length=200, default='')
    monthly_profit_aim = models.IntegerField(null=True, blank=True)
    date_registered = models.DateField(auto_now_add=True, editable=False)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
