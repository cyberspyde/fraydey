"""
Django management command to set up demo data
Run with: python manage.py setup_demo_data
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime, timedelta
from mnotes.models import Vendor, Profile, Product, ProductSold, BuyOnDebt
from mnotes.demo_data import DEMO_CREDENTIALS


class Command(BaseCommand):
    help = 'Sets up demo data for the application'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Setting up demo data...'))

        # Create or get demo user
        user, created = User.objects.get_or_create(
            username=DEMO_CREDENTIALS['username'],
            defaults={
                'email': 'demo@fraydey.uz',
            }
        )
        
        if created:
            user.set_password(DEMO_CREDENTIALS['password'])
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Created demo user: {user.username}'))
        else:
            self.stdout.write(self.style.WARNING(f'Demo user already exists: {user.username}'))

        # Create or update profile
        profile, created = Profile.objects.get_or_create(
            user=user,
            defaults={
                'bio': 'Bu demo akkount - Fraydey tizimining imkoniyatlarini ko\'rish uchun',
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created demo profile'))
        else:
            self.stdout.write(self.style.WARNING('Demo profile already exists'))

        # Create or update vendor
        vendor, created = Vendor.objects.get_or_create(
            username=DEMO_CREDENTIALS['username'],
            defaults={
                'vendor_name': 'Ali Valiyev',
                'vendor_email': 'demo@fraydey.uz',
                'vendor_tg': '@demo_vendor',
                'vendor_insta': '@demo_store',
                'vendor_phone_number': 998901234567,
                'store_name': 'Demo Fashion Store',
                'store_type': 'Kiyimlar',
                'store_website': 'https://fraydey.uz',
                'store_address': 'Toshkent, Chilonzor tumani',
                'monthly_profit_aim': 50000000,
                'password': DEMO_CREDENTIALS['password'],
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created demo vendor'))
        else:
            self.stdout.write(self.style.WARNING('Demo vendor already exists'))

        # Create demo products
        products_data = [
            {
                'product_name': 'Erkaklar ko\'ylagi',
                'product_price_initial': 150000,
                'product_price_told': 220000,
                'product_count': 25,
                'sold_count': 15,
                'discount': 10,
                'discount_in_sum': 22000,
            },
            {
                'product_name': 'Ayollar shim',
                'product_price_initial': 200000,
                'product_price_told': 300000,
                'product_count': 30,
                'sold_count': 22,
                'discount': 0,
                'discount_in_sum': 0,
            },
            {
                'product_name': 'Bolalar kurtka',
                'product_price_initial': 180000,
                'product_price_told': 260000,
                'product_count': 18,
                'sold_count': 12,
                'discount': 15,
                'discount_in_sum': 39000,
            },
            {
                'product_name': 'Sport futbolka',
                'product_price_initial': 80000,
                'product_price_told': 130000,
                'product_count': 50,
                'sold_count': 35,
                'discount': 0,
                'discount_in_sum': 0,
            },
            {
                'product_name': 'Qishki palto',
                'product_price_initial': 350000,
                'product_price_told': 520000,
                'product_count': 12,
                'sold_count': 8,
                'discount': 0,
                'discount_in_sum': 0,
                'isdebt': True,
            },
        ]

        for product_data in products_data:
            product, created = Product.objects.get_or_create(
                user=user,
                product_name=product_data['product_name'],
                defaults={
                    **product_data,
                    'datetime': timezone.now() - timedelta(days=30),
                    'last_discount_date': timezone.now(),
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created product: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.product_name}'))

        # Create demo sold products
        sold_products_data = [
            {
                'product_name': 'Erkaklar ko\'ylagi',
                'product_sold_price': 220000,
                'product_sold_count': 3,
                'profit': 210000,
                'customer_name': 'Akmal Toshmatov',
                'customer_phone': 998901111111,
                'paid_amount': 660000,
            },
            {
                'product_name': 'Ayollar shim',
                'product_sold_price': 300000,
                'product_sold_count': 2,
                'profit': 200000,
                'customer_name': 'Nodira Karimova',
                'customer_phone': 998902222222,
                'paid_amount': 600000,
            },
            {
                'product_name': 'Bolalar kurtka',
                'product_sold_price': 260000,
                'product_sold_count': 1,
                'profit': 80000,
                'customer_name': 'Shohruh Rahimov',
                'customer_phone': 998903333333,
                'paid_amount': 260000,
            },
        ]

        for sold_data in sold_products_data:
            sold_product, created = ProductSold.objects.get_or_create(
                username=DEMO_CREDENTIALS['username'],
                product_name=sold_data['product_name'],
                customer_name=sold_data['customer_name'],
                defaults={
                    **sold_data,
                    'isdebt': False,
                    'isfullypaid': True,
                    'ispartlypaid': False,
                    'left_amount': 0,
                    'date_sold': timezone.now().date(),
                }
            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Created sold product: {sold_product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Sold product already exists: {sold_product.product_name}'))

        # Create demo debt product
        debt_product, created = ProductSold.objects.get_or_create(
            username=DEMO_CREDENTIALS['username'],
            product_name='Qishki palto',
            customer_name='Dilshod Yusupov',
            defaults={
                'product_sold_price': 520000,
                'product_sold_count': 2,
                'profit': 340000,
                'isdebt': True,
                'isfullypaid': False,
                'ispartlypaid': True,
                'paid_amount': 520000,
                'left_amount': 520000,
                'customer_phone': 998904444444,
                'date_sold': (timezone.now() - timedelta(days=5)).date(),
                'due_date': (timezone.now() + timedelta(days=25)).date(),
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created debt sold product'))
        else:
            self.stdout.write(self.style.WARNING('Debt sold product already exists'))

        # Create demo buy on debt
        buy_debt, created = BuyOnDebt.objects.get_or_create(
            username=DEMO_CREDENTIALS['username'],
            product_name='Qishki palto',
            owner_name='Farruh Wholesaler',
            defaults={
                'product_bought_count': 20,
                'product_bought_price': 350000,
                'owner_phone': 998905555555,
                'date_bought': (timezone.now() - timedelta(days=10)).date(),
                'due_date': (timezone.now() + timedelta(days=20)).date(),
                'isfullypaid': False,
                'ispartlypaid': True,
                'paid_amount': 3500000,
                'left_amount': 3500000,
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created buy on debt record'))
        else:
            self.stdout.write(self.style.WARNING('Buy on debt record already exists'))

        self.stdout.write(self.style.SUCCESS('\n=== Demo data setup complete! ==='))
        self.stdout.write(self.style.SUCCESS(f'Username: {DEMO_CREDENTIALS["username"]}'))
        self.stdout.write(self.style.SUCCESS(f'Password: {DEMO_CREDENTIALS["password"]}'))
