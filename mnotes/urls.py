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
	path('sales/', views.sales, name='sales'),
	path('createproduct/', views.createproduct, name='createproduct'),
    path('signup/', signup.as_view(), name='signup'),
    path('login/', login.as_view(redirect_authenticated_user=True, template_name='mnotes/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mnotes/index.html'), name='logout'),
   	path('profile', profile, name='profile'),
   	path('password-change/', changepassword.as_view(), name='password_change'),
   	path('productview/<int:id>', views.productview, name='productview'),
	path('editproduct/<int:id>', views.editproduct, name='editproduct'),
	path('searchfunction', views.searchfunction, name='searchfunction'),
	path('searchbuydebt', views.searchbuydebt, name='searchbuydebt'),
	path('searchselldebt', views.searchselldebt, name='searchselldebt'),
	path('deleteproduct/<int:id>', views.deleteproduct, name='deleteproduct'),
	path('sellproduct/', views.sellproduct, name='sellproduct'),
	path('productsold/<int:id>', views.productsold, name='productsold'),
	path('debts/', views.debts, name='debts'),
	path('givedebt/<int:id>', views.givedebt, name='givedebt'),
	path('getdebt/<int:id>', views.getdebt, name='getdebt'),
	path('getdebtselect/', views.getdebtselect, name='getdebtselect'),
	path('givedebtselect/', views.givedebtselect, name='givedebtselect'),
	path('paydebt/<int:id>', views.paydebt, name='paydebt'),
	path('returndebt/<int:id>', views.returndebt, name='returndebt'),
	path('editprofile/<str:username>', views.editprofile, name='editprofile'),
	path('selldebtview/<int:id>', views.selldebtview, name='selldebtview'),
	path('buydebtview/<int:id>', views.buydebtview, name='buydebtview'),
	path('searchsoldproduct', views.searchsoldproduct, name='searchsoldproduct'),
	path('searchbuydebtselect', views.searchbuydebtselect, name='searchbuydebtselect'),
	path('searchselldebtselect', views.searchselldebtselect, name='searchselldebtselect'),
	path('soldproducts', views.soldproducts, name='soldproducts'),
	path('soldproductview/<int:id>', views.soldproductview, name='soldproductview'),
	path('analytics', views.analytics, name='analytics'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#urlpatterns += staticfiles_urlpatterns()

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
