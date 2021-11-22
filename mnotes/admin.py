from django.contrib import admin
from .models import Notes, Profile, Product, ProductSold, BuyOnDebt, SellOnDebt, Vendor
from .forms import NotesForm, ProductForm, ProductSoldForm
# Register your models here.

class ComputerAdmin(admin.ModelAdmin):
	list_display = ['pub_date']
	form = NotesForm


class ProductAdmin(admin.ModelAdmin):
	list_display = ['user', 'product_name', 'id']
	form = ProductForm

class ProductSoldAdmin(admin.ModelAdmin):
	list_display = ['product_sold_id', 'product_sold_price', 'product_sold_count', 'date_sold']
	form = ProductSoldForm

class SellOnDebtAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'customer_name', 'due_date', 'given_date']

class BuyOnDebtAdmin(admin.ModelAdmin):
	list_display = ['id','product_name', 'owner_name', 'date_bought']

class VendorAdmin(admin.ModelAdmin):
	list_display = ['username', 'vendor_name', 'store_type']

admin.site.register(Notes, ComputerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSold, ProductSoldAdmin)
admin.site.register(SellOnDebt, SellOnDebtAdmin)
admin.site.register(BuyOnDebt, BuyOnDebtAdmin)
admin.site.register(Vendor, VendorAdmin)

