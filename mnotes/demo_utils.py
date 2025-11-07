"""
Demo Mode Views Wrapper
Wraps views to use demo data instead of database queries
"""

from django.conf import settings
from .demo_data import (
    get_demo_user, 
    get_demo_profile,
    get_demo_vendor,
    get_demo_products,
    get_demo_sold_products,
    get_demo_buy_on_debt,
    DEMO_CREDENTIALS
)


class DemoQuerySet:
    """Mock QuerySet for demo mode"""
    
    def __init__(self, data):
        self._data = data if isinstance(data, list) else [data]
    
    def filter(self, **kwargs):
        """Mock filter - returns filtered data"""
        if not kwargs:
            return self
        
        filtered = self._data
        for key, value in kwargs.items():
            # Handle user and username lookups
            if key in ['user', 'user_id']:
                if hasattr(value, 'id'):
                    filtered = [item for item in filtered if hasattr(item, 'user_id') and item.user_id == value.id]
                else:
                    filtered = [item for item in filtered if hasattr(item, 'user_id') and item.user_id == value]
            elif key == 'username':
                filtered = [item for item in filtered if hasattr(item, 'username') and item.username == value]
            elif key == 'pk':
                filtered = [item for item in filtered if hasattr(item, 'id') and item.id == value]
            elif '__' in key:
                # Handle field lookups like product_name__contains
                field, lookup = key.split('__', 1)
                if lookup == 'contains':
                    filtered = [item for item in filtered if hasattr(item, field) and value.lower() in str(getattr(item, field)).lower()]
            else:
                filtered = [item for item in filtered if hasattr(item, key) and getattr(item, key) == value]
        
        return DemoQuerySet(filtered)
    
    def get(self, **kwargs):
        """Mock get - returns single object"""
        filtered = self.filter(**kwargs)
        if len(filtered._data) == 0:
            from django.core.exceptions import ObjectDoesNotExist
            raise ObjectDoesNotExist("Object does not exist in demo data")
        return filtered._data[0]
    
    def all(self):
        """Mock all - returns all data"""
        return self
    
    def count(self):
        """Mock count"""
        return len(self._data)
    
    def __iter__(self):
        """Allow iteration"""
        return iter(self._data)
    
    def __len__(self):
        """Return length"""
        return len(self._data)
    
    def __getitem__(self, index):
        """Allow indexing"""
        return self._data[index]


def get_demo_objects_for_model(model_name, user=None):
    """
    Get demo objects for a specific model
    """
    demo_user = get_demo_user()
    
    if model_name == 'Product':
        return DemoQuerySet(get_demo_products(demo_user))
    elif model_name == 'ProductSold':
        return DemoQuerySet(get_demo_sold_products(DEMO_CREDENTIALS['username']))
    elif model_name == 'BuyOnDebt':
        return DemoQuerySet(get_demo_buy_on_debt(DEMO_CREDENTIALS['username']))
    elif model_name == 'Vendor':
        vendor = get_demo_vendor(DEMO_CREDENTIALS['username'])
        return DemoQuerySet([vendor] if vendor else [])
    elif model_name == 'Profile':
        profile = get_demo_profile(demo_user)
        return DemoQuerySet([profile])
    elif model_name == 'Customer':
        return DemoQuerySet([])
    elif model_name == 'Notes':
        return DemoQuerySet([])
    else:
        return DemoQuerySet([])


def is_demo_mode():
    """Check if demo mode is enabled"""
    return getattr(settings, 'DEMO_MODE', False)
