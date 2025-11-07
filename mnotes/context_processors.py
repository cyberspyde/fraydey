"""
Context processors for demo mode
Makes demo mode available in all templates
"""

from django.conf import settings


def demo_mode(request):
    """
    Add demo mode status to template context
    """
    return {
        'DEMO_MODE': getattr(settings, 'DEMO_MODE', False),
        'demo_mode': getattr(settings, 'DEMO_MODE', False),
    }
