from django.contrib import admin
from .models import Notes, Profile, Product, ProductSold, BuyOnDebt, SellOnDebt
from .forms import NotesForm, ProductForm, ProductSoldForm
# Register your models here.

class ComputerAdmin(admin.ModelAdmin):
	list_display = ['pub_date']
	form = NotesForm


class ProductAdmin(admin.ModelAdmin):
	list_display = ['user', 'product_name', 'id']
	form = ProductForm

class ProductSoldAdmin(admin.ModelAdmin):
	list_display = ['product_sold_id', 'product_sold_price', 'product_sold_count', 'profit']
	form = ProductSoldForm

class SellOnDebtAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'customer_name', 'user', 'due_date', 'given_date']

class BuyOnDebtAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'owner_name', 'user', 'date_bought']

admin.site.register(Notes, ComputerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductSold, ProductSoldAdmin)
admin.site.register(SellOnDebt, SellOnDebtAdmin)
admin.site.register(BuyOnDebt, BuyOnDebtAdmin)