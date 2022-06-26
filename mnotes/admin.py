from django.contrib import admin
from .models import Notes, Profile, Product, ProductSold, BuyOnDebt, Vendor, Customer
from .forms import NotesForm, ProductForm, ProductSoldForm
# Register your models here.

class ComputerAdmin(admin.ModelAdmin):
	list_display = ['pub_date']
	form = NotesForm


class ProductAdmin(admin.ModelAdmin):
	list_display = ['user', 'product_name', 'discount']
	form = ProductForm

class ProductSoldAdmin(admin.ModelAdmin):
	list_display = ['username', 'product_sold_price', 'date_sold', 'id']
	form = ProductSoldForm

class SellOnDebtAdmin(admin.ModelAdmin):
	list_display = ['username', 'product_name', 'customer_name', 'id']

class BuyOnDebtAdmin(admin.ModelAdmin):
	list_display = ['id','product_name', 'owner_name', 'date_bought']

class VendorAdmin(admin.ModelAdmin):
	list_display = ['username', 'vendor_name', 'store_type']

class CustomerAdmin(admin.ModelAdmin):
	list_display = ['username', 'customer_name', 'date_registered']



#admin.site.register(Notes, ComputerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSold, ProductSoldAdmin)
admin.site.register(BuyOnDebt, BuyOnDebtAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Customer, CustomerAdmin)

