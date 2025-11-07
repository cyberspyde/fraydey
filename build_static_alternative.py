"""
Alternative Static Site Builder
Manually renders Django pages to static HTML
"""

import os
from pathlib import Path
from django.test import RequestFactory
from django.conf import settings
from mnotes import views
from mnotes.demo_data import DEMO_PRODUCTS, DEMO_SOLD_PRODUCTS, DEMO_BUY_ON_DEBT


def build_static_pages():
    """Build static pages manually"""
    print("Using alternative static builder...")
    
    dist_dir = settings.DISTILL_DIR
    dist_dir.mkdir(exist_ok=True)
    
    factory = RequestFactory()
    
    # Pages to build
    pages = [
        ('dashboard', views.dashboard, 'dashboard/index.html'),
        ('inventory', views.inventory, 'inventory/index.html'),
        ('profile', views.profile, 'profile/index.html'),
        ('soldproducts', views.soldproducts, 'soldproducts/index.html'),
        ('sellondebts', views.sellondebts, 'sellondebts/index.html'),
        ('buyondebts', views.buyondebts, 'buyondebts/index.html'),
        ('viewdiscounts', views.viewdiscounts, 'viewdiscounts/index.html'),
        ('reports', views.reports, 'reports/index.html'),
    ]
    
    for name, view_func, output_path in pages:
        try:
            print(f"  Building {name}...")
            request = factory.get(f'/{name}')
            request.user = type('User', (), {
                'is_authenticated': True,
                'id': 1,
                'username': 'demo'
            })()
            request.demo_mode = True
            
            response = view_func(request)
            
            output_file = dist_dir / output_path
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'wb') as f:
                f.write(response.content)
            
            print(f"    ✓ {output_path}")
        except Exception as e:
            print(f"    ✗ Error: {e}")
    
    # Build product detail pages
    print("  Building product pages...")
    for product in DEMO_PRODUCTS:
        try:
            product_id = product['id']
            request = factory.get(f'/productview/{product_id}')
            request.user = type('User', (), {
                'is_authenticated': True,
                'id': 1,
                'username': 'demo'
            })()
            request.demo_mode = True
            
            response = views.productview(request, product_id)
            
            output_file = dist_dir / f'productview/{product_id}/index.html'
            output_file.parent.mkdir(parents=True, exist_ok=True)
            
            with open(output_file, 'wb') as f:
                f.write(response.content)
            
            print(f"    ✓ productview/{product_id}/")
        except Exception as e:
            print(f"    ✗ Error for product {product_id}: {e}")
    
    print("✅ Alternative build complete")


if __name__ == '__main__':
    import django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MarketingNotes.settings')
    django.setup()
    build_static_pages()
