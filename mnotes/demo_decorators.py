"""
Demo Mode Decorators
Decorators to handle demo mode in views
"""

from functools import wraps
from django.conf import settings
from django.contrib import messages
from .demo_utils import get_demo_objects_for_model, is_demo_mode
from .demo_data import get_demo_user, get_demo_profile, get_demo_vendor


def demo_mode_handler(view_func):
    """
    Decorator to handle demo mode in views
    Intercepts model queries and uses demo data instead
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if is_demo_mode():
            # Inject demo mode flag into request
            request.is_demo = True
            
            # Override the user object with demo user
            if request.user.is_authenticated:
                request.demo_user = get_demo_user()
        else:
            request.is_demo = False
        
        return view_func(request, *args, **kwargs)
    
    return wrapper


def prevent_demo_writes(view_func):
    """
    Decorator to prevent write operations in demo mode
    Shows a warning message instead
    """
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if is_demo_mode() and request.method == 'POST':
            messages.warning(
                request, 
                "Bu demo rejim. Ma'lumotlar o'zgartirilmaydi. "
                "Real tizimda bu amal bajarilar edi."
            )
            # Still call the view but it should handle demo mode internally
        
        return view_func(request, *args, **kwargs)
    
    return wrapper
