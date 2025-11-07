"""MarketingNotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings

# Use distill URLs for static generation in demo mode
if getattr(settings, 'DEMO_MODE', False):
    try:
        # Try to import distill URLs for static generation
        from mnotes import distill_urls as mnotes_urls_module
    except ImportError:
        # Fallback to regular URLs if distill not available
        from mnotes import urls as mnotes_urls_module
else:
    from mnotes import urls as mnotes_urls_module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(mnotes_urls_module)),
]
