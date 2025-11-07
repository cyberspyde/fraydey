"""
Django Distill URL Configuration
Defines which URLs to render as static files
"""
from django_distill import distill_path
from django.urls import path
from django.contrib.auth import views as auth_views
from mnotes import views
from mnotes.views import login, signup

def get_none():
    """Return None for pages that don't need parameters"""
    return None

def get_product_ids():
    """Get all product IDs for static generation"""
    from mnotes.demo_data import DEMO_PRODUCTS
    return [{'id': p['id']} for p in DEMO_PRODUCTS]

def get_soldproduct_ids():
    """Get all sold product IDs"""
    from mnotes.demo_data import DEMO_SOLD_PRODUCTS
    return [{'id': p['id']} for p in DEMO_SOLD_PRODUCTS]

def get_debt_ids():
    """Get all debt IDs for sell debts"""
    from mnotes.demo_data import DEMO_SOLD_PRODUCTS
    sell_debts = [{'id': p['id']} for p in DEMO_SOLD_PRODUCTS if p.get('isdebt')]
    return sell_debts if sell_debts else [{'id': 1}]

def get_buy_debt_ids():
    """Get all debt IDs for buy debts"""
    from mnotes.demo_data import DEMO_BUY_ON_DEBT
    return [{'id': p['id']} for p in DEMO_BUY_ON_DEBT] if DEMO_BUY_ON_DEBT else [{'id': 1}]

def get_username():
    """Get demo username"""
    return [{'username': 'demo'}]

# Static URL patterns for demo mode
urlpatterns = [
    # Auth pages (regular path, not distilled)
    path('login/', login.as_view(template_name='mnotes/vendorpages/login.html'), name='login'),
    path('signup/', signup.as_view(), name='signup'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mnotes/index.html'), name='logout'),
    path('password-change/', views.changepassword.as_view(), name='password_change'),
    
    # Main pages
    distill_path('', views.index, name='index', distill_func=get_none),
    distill_path('dashboard', views.dashboard, name='dashboard', distill_func=get_none),
    distill_path('inventory/', views.inventory, name='inventory', distill_func=get_none),
    distill_path('profile', views.profile, name='profile', distill_func=get_none),
    
    # Product pages
    distill_path('createproduct/', views.createproduct, name='createproduct', distill_func=get_none),
    distill_path('productview/<int:id>', views.productview, name='productview', distill_func=get_product_ids),
    distill_path('editproduct/<int:id>', views.editproduct, name='editproduct', distill_func=get_product_ids),
    distill_path('deleteproduct/<int:id>', views.deleteproduct, name='deleteproduct', distill_func=get_product_ids),
    distill_path('selectsoldproduct', views.selectsoldproduct, name='selectsoldproduct', distill_func=get_none),
    
    # Sales pages
    distill_path('soldproducts', views.soldproducts, name='soldproducts', distill_func=get_none),
    distill_path('soldproductview/<int:id>', views.soldproductview, name='soldproductview', distill_func=get_soldproduct_ids),
    distill_path('productsold/<int:id>', views.productsold, name='productsold', distill_func=get_product_ids),
    
    # Debt pages
    distill_path('sellondebts', views.sellondebts, name='sellondebts', distill_func=get_none),
    distill_path('buyondebts', views.buyondebts, name='buyondebts', distill_func=get_none),
    distill_path('selldebtselect/', views.selldebtselect, name='selldebtselect', distill_func=get_none),
    distill_path('buydebtselect/', views.buydebtselect, name='buydebtselect', distill_func=get_none),
    distill_path('selldebtview/<int:id>', views.selldebtview, name='selldebtview', distill_func=get_debt_ids),
    distill_path('buydebtview/<int:id>', views.buydebtview, name='buydebtview', distill_func=get_buy_debt_ids),
    distill_path('selldebt/<int:id>', views.selldebt, name='selldebt', distill_func=get_product_ids),
    distill_path('buydebt/<int:id>', views.buydebt, name='buydebt', distill_func=get_product_ids),
    distill_path('paydebt/<int:id>', views.paydebt, name='paydebt', distill_func=get_buy_debt_ids),
    distill_path('returndebt/<int:id>', views.returndebt, name='returndebt', distill_func=get_debt_ids),
    
    # Profile pages
    distill_path('editprofile/<str:username>', views.editprofile, name='editprofile', distill_func=get_username),
    
    # Other pages
    distill_path('viewdiscounts', views.viewdiscounts, name='viewdiscounts', distill_func=get_none),
    distill_path('creatediscountselect', views.creatediscountselect, name='creatediscountselect', distill_func=get_none),
    distill_path('creatediscount/<int:id>', views.creatediscount, name='creatediscount', distill_func=get_soldproduct_ids),
    distill_path('reports', views.reports, name='reports', distill_func=get_none),
]
