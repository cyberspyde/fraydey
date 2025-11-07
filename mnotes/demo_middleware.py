"""
Demo Mode Middleware
Handles authentication and data interception in demo mode
"""

from django.conf import settings
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.urls import reverse
from .demo_data import DEMO_CREDENTIALS, get_demo_user


class DemoModeMiddleware:
    """
    Middleware to handle demo mode
    - Auto-login demo user
    - Intercept write operations
    - Show demo mode banner
    """
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # Check if demo mode is enabled
        demo_mode = getattr(settings, 'DEMO_MODE', False)
        
        if demo_mode:
            # Add demo mode flag to request
            request.demo_mode = True
            
            # Auto-login demo user if not authenticated and not on logout page
            if not request.user.is_authenticated and request.path != reverse('logout'):
                # Create or get demo user
                demo_user = self._get_or_create_demo_user()
                if demo_user and request.path not in [reverse('login'), reverse('signup')]:
                    # Set the backend attribute to allow login
                    demo_user.backend = 'django.contrib.auth.backends.ModelBackend'
                    auth_login(request, demo_user)
        else:
            request.demo_mode = False
        
        response = self.get_response(request)
        
        # Add demo mode header
        if demo_mode:
            response['X-Demo-Mode'] = 'true'
        
        return response
    
    def _get_or_create_demo_user(self):
        """Get or create the demo user"""
        try:
            user = User.objects.get(username=DEMO_CREDENTIALS['username'])
            return user
        except User.DoesNotExist:
            # Create demo user if it doesn't exist
            user = User.objects.create_user(
                username=DEMO_CREDENTIALS['username'],
                password=DEMO_CREDENTIALS['password'],
                email='demo@fraydey.uz'
            )
            return user
