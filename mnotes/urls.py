from django.urls import path
from django.contrib.auth import views as auth_views
from .views import login, signup, profile, changepassword
from .forms import LoginForm, SignUpForm
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('', views.index, name='index'),
	path('takenote/', views.takenote, name='takenote'),
	path('takenoteview/', views.takenoteview, name='takenoteview'),
	path('savednotes/', views.savednotes, name='savednotes'),
	path('inventory/', views.inventory, name='inventory'),
	path('createproduct/', views.createproduct, name='createproduct'),
    path('signup/', signup.as_view(), name='signup'),
    path('login/', login.as_view(redirect_authenticated_user=True, template_name='mnotes/vendorpages/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mnotes/index.html'), name='logout'),
   	path('profile', profile, name='profile'),
   	path('password-change/', changepassword.as_view(), name='password_change'),
   	path('productview/<int:id>', views.productview, name='productview'),
	path('editproduct/<int:id>', views.editproduct, name='editproduct'),
	path('deleteproduct/<int:id>', views.deleteproduct, name='deleteproduct'),
	path('productsold/<int:id>', views.productsold, name='productsold'),
	path('selldebt/<int:id>', views.selldebt, name='selldebt'),
	path('buydebt/<int:id>', views.buydebt, name='buydebt'),
	path('buydebtselect/', views.buydebtselect, name='buydebtselect'),
	path('selldebtselect/', views.selldebtselect, name='selldebtselect'),
	path('paydebt/<int:id>', views.paydebt, name='paydebt'),
	path('returndebt/<int:id>', views.returndebt, name='returndebt'),
	path('editprofile/<str:username>', views.editprofile, name='editprofile'),
	path('selldebtview/<int:id>', views.selldebtview, name='selldebtview'),
	path('buydebtview/<int:id>', views.buydebtview, name='buydebtview'),
	path('soldproducts', views.soldproducts, name='soldproducts'),
	path('soldproductview/<int:id>', views.soldproductview, name='soldproductview'),
	path('signupselect', views.signupselect, name='signupselect'),
	path('dashboard', views.dashboard, name='dashboard'),
	path('customerdashboard', views.customerdashboard, name='customerdashboard'),
	path('buyondebts', views.buyondebts, name='buyondebts'),
	path('sellondebts', views.sellondebts, name='sellondebts'),
	path('selectsoldproduct', views.selectsoldproduct, name='selectsoldproduct'),
	path('creatediscount/<int:id>', views.creatediscount, name='creatediscount'),
	path('creatediscountselect', views.creatediscountselect, name='creatediscountselect'),
	path('viewdiscounts', views.viewdiscounts, name='viewdiscounts'),
	path('reports', views.reports, name='reports'),

	path('customerdashboard', views.customerdashboard, name='customerdashboard'),
	path('customerprofile', views.customerprofile, name='customerprofile'),
	path('vendors', views.vendors, name='vendors'),
	path('view_vendor/<int:vendor_id>', views.view_vendor, name='view_vendor'),
	path('customercontact', views.customercontact, name='customercontact')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
