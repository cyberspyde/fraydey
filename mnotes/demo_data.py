"""
Demo data for demonstration mode
This module contains pre-populated data to showcase the application without database connections
"""

from datetime import datetime, timedelta
from django.utils import timezone

# Demo user credentials
DEMO_CREDENTIALS = {
    'username': 'demo',
    'password': 'demo123',
    'user_id': 1,
}

# Demo vendor data
DEMO_VENDOR = {
    'id': 1,
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
    'username': 'demo',
    'password': 'demo123',
    'date_registered': datetime.now().date(),
}

# Demo profile
DEMO_PROFILE = {
    'id': 1,
    'user_id': 1,
    'bio': 'Bu demo akkount - Fraydey tizimining imkoniyatlarini ko\'rish uchun',
    'image': 'demo-images/profile.jpeg',
}

# Demo products
DEMO_PRODUCTS = [
    {
        'id': 1,
        'user_id': 1,
        'product_name': 'Erkaklar ko\'ylagi',
        'product_price_initial': 150000,
        'product_price_told': 220000,
        'product_count': 25,
        'product_img': 'demo-images/erkaklar-koylagi.jpeg',
        'datetime': datetime.now() - timedelta(days=30),
        'isdebt': False,
        'sold_count': 15,
        'discount': 10,
        'discount_in_sum': 22000,
        'last_discount_date': datetime.now(),
    },
    {
        'id': 2,
        'user_id': 1,
        'product_name': 'Ayollar shim',
        'product_price_initial': 200000,
        'product_price_told': 300000,
        'product_count': 30,
        'product_img': 'demo-images/ayollar-shim.jpeg',
        'datetime': datetime.now() - timedelta(days=25),
        'isdebt': False,
        'sold_count': 22,
        'discount': 0,
        'discount_in_sum': 0,
        'last_discount_date': datetime.now() - timedelta(days=20),
    },
    {
        'id': 3,
        'user_id': 1,
        'product_name': 'Bolalar kurtka',
        'product_price_initial': 180000,
        'product_price_told': 260000,
        'product_count': 18,
        'product_img': 'demo-images/bolalar-kurtka.jpeg',
        'datetime': datetime.now() - timedelta(days=20),
        'isdebt': False,
        'sold_count': 12,
        'discount': 15,
        'discount_in_sum': 39000,
        'last_discount_date': datetime.now(),
    },
    {
        'id': 4,
        'user_id': 1,
        'product_name': 'Sport futbolka',
        'product_price_initial': 80000,
        'product_price_told': 130000,
        'product_count': 50,
        'product_img': 'demo-images/sport-futbolka.jpeg',
        'datetime': datetime.now() - timedelta(days=15),
        'isdebt': False,
        'sold_count': 35,
        'discount': 0,
        'discount_in_sum': 0,
        'last_discount_date': datetime.now() - timedelta(days=10),
    },
    {
        'id': 5,
        'user_id': 1,
        'product_name': 'Qishki palto',
        'product_price_initial': 350000,
        'product_price_told': 520000,
        'product_count': 12,
        'product_img': 'demo-images/qishki-palto.jpeg',
        'datetime': datetime.now() - timedelta(days=10),
        'isdebt': True,
        'sold_count': 8,
        'discount': 0,
        'discount_in_sum': 0,
        'last_discount_date': datetime.now() - timedelta(days=5),
    },
]

# Demo sold products
DEMO_SOLD_PRODUCTS = [
    {
        'id': 1,
        'product_sold_price': 220000,
        'product_sold_count': 3,
        'product_name': 'Erkaklar ko\'ylagi',
        'profit': 210000,
        'isdebt': False,
        'isfullypaid': True,
        'ispartlypaid': False,
        'paid_amount': 660000,
        'left_amount': 0,
        'username': 'demo',
        'date_sold': datetime.now().date(),
        'customer_phone': 998901111111,
        'customer_name': 'Akmal Toshmatov',
        'due_date': None,
    },
    {
        'id': 2,
        'product_sold_price': 300000,
        'product_sold_count': 2,
        'product_name': 'Ayollar shim',
        'profit': 200000,
        'isdebt': False,
        'isfullypaid': True,
        'ispartlypaid': False,
        'paid_amount': 600000,
        'left_amount': 0,
        'username': 'demo',
        'date_sold': datetime.now().date(),
        'customer_phone': 998902222222,
        'customer_name': 'Nodira Karimova',
        'due_date': None,
    },
    {
        'id': 3,
        'product_sold_price': 260000,
        'product_sold_count': 1,
        'product_name': 'Bolalar kurtka',
        'profit': 80000,
        'isdebt': False,
        'isfullypaid': True,
        'ispartlypaid': False,
        'paid_amount': 260000,
        'left_amount': 0,
        'username': 'demo',
        'date_sold': datetime.now().date() - timedelta(days=1),
        'customer_phone': 998903333333,
        'customer_name': 'Shohruh Rahimov',
        'due_date': None,
    },
    {
        'id': 4,
        'product_sold_price': 520000,
        'product_sold_count': 2,
        'product_name': 'Qishki palto',
        'profit': 340000,
        'isdebt': True,
        'isfullypaid': False,
        'ispartlypaid': True,
        'paid_amount': 520000,
        'left_amount': 520000,
        'username': 'demo',
        'date_sold': datetime.now().date() - timedelta(days=5),
        'customer_phone': 998904444444,
        'customer_name': 'Dilshod Yusupov',
        'due_date': datetime.now().date() + timedelta(days=25),
    },
]

# Demo buy on debt records
DEMO_BUY_ON_DEBT = [
    {
        'id': 1,
        'product_name': 'Qishki palto',
        'product_bought_count': 20,
        'product_bought_price': 350000,
        'owner_name': 'Farruh Wholesaler',
        'owner_phone': 998905555555,
        'date_bought': datetime.now().date() - timedelta(days=10),
        'due_date': datetime.now().date() + timedelta(days=20),
        'username': 'demo',
        'isfullypaid': False,
        'ispartlypaid': True,
        'paid_amount': 3500000,
        'left_amount': 3500000,
    },
]

# Demo customers
DEMO_CUSTOMERS = [
    {
        'id': 1,
        'customer_name': 'Akmal Toshmatov',
        'customer_email': 'akmal@example.com',
        'customer_phone_number': 998901111111,
        'customer_insta': '@akmal_t',
        'customer_tg': '@akmal_toshmatov',
        'username': 'democustomer',
        'password': 'demo123',
        'date_registered': datetime.now().date(),
    },
]

# Demo notes
DEMO_NOTES = [
    {
        'id': 1,
        'pub_date': datetime.now() - timedelta(days=5),
    },
]

def get_demo_user():
    """Returns a demo user object"""
    class DemoUser:
        def __init__(self):
            self.id = DEMO_CREDENTIALS['user_id']
            self.username = DEMO_CREDENTIALS['username']
            self.is_authenticated = True
            self.is_active = True
            self.is_staff = False
            self.is_superuser = False
            
        def __str__(self):
            return self.username
    
    return DemoUser()

def get_demo_profile(user):
    """Returns a demo profile object"""
    class DemoImageField:
        def __init__(self, path):
            self.name = path
            self.path = path
            
        @property
        def url(self):
            if self.name:
                return f'/media/{self.name}'
            return ''
            
        def __bool__(self):
            return bool(self.name)
    
    class DemoProfile:
        def __init__(self, profile_data):
            self.id = profile_data['id']
            self.user = user
            self.bio = profile_data['bio']
            self.image = DemoImageField(profile_data['image']) if profile_data['image'] else None
            
        def __str__(self):
            return self.user.username
    
    return DemoProfile(DEMO_PROFILE)

def get_demo_vendor(username):
    """Returns a demo vendor object"""
    class DemoVendor:
        def __init__(self, vendor_data):
            for key, value in vendor_data.items():
                setattr(self, key, value)
        
        def __str__(self):
            return self.vendor_name
    
    if username == DEMO_CREDENTIALS['username']:
        return DemoVendor(DEMO_VENDOR)
    return None

def get_demo_products(user):
    """Returns demo product objects"""
    class DemoImageField:
        def __init__(self, path):
            self.name = path
            self.path = path
            
        @property
        def url(self):
            if self.name:
                return f'/media/{self.name}'
            return ''
            
        def __bool__(self):
            return bool(self.name)
    
    class DemoProduct:
        def __init__(self, product_data):
            for key, value in product_data.items():
                if key == 'product_img':
                    setattr(self, key, DemoImageField(value) if value else None)
                else:
                    setattr(self, key, value)
            self.user = user
        
        def __str__(self):
            return self.product_name
        
        def save(self, *args, **kwargs):
            # Mock save method for demo mode
            pass
    
    return [DemoProduct(p) for p in DEMO_PRODUCTS]

def get_demo_sold_products(username):
    """Returns demo sold product objects"""
    class DemoProductSold:
        def __init__(self, sold_data):
            for key, value in sold_data.items():
                setattr(self, key, value)
        
        def save(self, *args, **kwargs):
            # Mock save method for demo mode
            pass
    
    return [DemoProductSold(s) for s in DEMO_SOLD_PRODUCTS]

def get_demo_buy_on_debt(username):
    """Returns demo buy on debt objects"""
    class DemoBuyOnDebt:
        def __init__(self, debt_data):
            for key, value in debt_data.items():
                setattr(self, key, value)
        
        def save(self, *args, **kwargs):
            # Mock save method for demo mode
            pass
    
    return [DemoBuyOnDebt(d) for d in DEMO_BUY_ON_DEBT]
