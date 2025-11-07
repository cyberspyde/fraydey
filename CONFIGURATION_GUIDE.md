# Demo Mode Configuration Reference

## Quick Reference

### Enable Demo Mode
```python
# In MarketingNotes/settings.py
DEMO_MODE = True
```

### Disable Demo Mode
```python
# In MarketingNotes/settings.py
DEMO_MODE = False
```

## Complete Configuration

### 1. Settings (MarketingNotes/settings.py)

```python
# Demo Mode Configuration
# Set to True to enable demo mode with pre-populated data and no database writes
DEMO_MODE = True

# Middleware Configuration (Order matters!)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'mnotes.demo_middleware.DemoModeMiddleware',  # Add this line
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Template Configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mnotes.context_processors.demo_mode',  # Add this line
            ],
        },
    },
]
```

### 2. Demo Credentials (mnotes/demo_data.py)

```python
# Default demo credentials
DEMO_CREDENTIALS = {
    'username': 'demo',
    'password': 'demo123',
    'user_id': 1,
}
```

**To customize:**
```python
# Change to your preferred demo credentials
DEMO_CREDENTIALS = {
    'username': 'your_username',
    'password': 'your_password',
    'user_id': 1,
}
```

### 3. Demo Vendor Information (mnotes/demo_data.py)

```python
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
```

## Environment-Specific Configuration

### Development Environment
```python
# settings.py or settings_dev.py
DEBUG = True
DEMO_MODE = True  # Enable for demos
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
```

### Staging Environment
```python
# settings_staging.py
DEBUG = True
DEMO_MODE = True  # Can be enabled for client demos
ALLOWED_HOSTS = ['staging.yourdomain.com']
```

### Production Environment
```python
# settings_prod.py
DEBUG = False
DEMO_MODE = False  # ⚠️ MUST BE FALSE IN PRODUCTION!
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
```

## Using Environment Variables

For better security and flexibility, use environment variables:

```python
# settings.py
import os

# Demo mode from environment variable (defaults to False)
DEMO_MODE = os.getenv('DEMO_MODE', 'False').lower() == 'true'
```

Then set in your environment:

**Windows (PowerShell):**
```powershell
$env:DEMO_MODE = "True"
python manage.py runserver
```

**Windows (CMD):**
```cmd
set DEMO_MODE=True
python manage.py runserver
```

**Linux/Mac:**
```bash
export DEMO_MODE=True
python manage.py runserver
```

## Docker Configuration

If using Docker, add to your `docker-compose.yml`:

```yaml
version: '3.8'

services:
  web:
    build: .
    environment:
      - DEMO_MODE=True  # Set to False for production
      - SECRET_KEY=${SECRET_KEY}
    ports:
      - "8000:8000"
    command: python manage.py runserver 0.0.0.0:8000
```

Or in `.env` file:
```env
DEMO_MODE=True
SECRET_KEY=your-secret-key-here
```

## Advanced Configuration

### Custom Demo Data Path

If you want to load demo data from a different file:

```python
# settings.py
DEMO_DATA_MODULE = 'mnotes.demo_data'  # Default
# Or:
# DEMO_DATA_MODULE = 'myapp.custom_demo_data'
```

### Demo Mode Banner Customization

Edit `mnotes/templates/mnotes/demo_banner.html`:

```html
<!-- Custom colors and styling -->
<div class="demo-mode-banner" style="
    background: linear-gradient(135deg, #YOUR_COLOR1 0%, #YOUR_COLOR2 100%);
    color: white;
    padding: 15px 20px;
    /* ... other styles ... */
">
    <strong>YOUR CUSTOM MESSAGE</strong>
</div>
```

### Demo Session Timeout

Add to `settings.py`:

```python
# Demo mode specific settings
if DEMO_MODE:
    # Short session for demos (15 minutes)
    SESSION_COOKIE_AGE = 60 * 15
    # Auto-logout on browser close
    SESSION_EXPIRE_AT_BROWSER_CLOSE = True
```

### Demo Mode Logging

Add logging configuration:

```python
# settings.py
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'demo_file': {
            'class': 'logging.FileHandler',
            'filename': 'demo_mode.log',
        },
    },
    'loggers': {
        'mnotes.demo_middleware': {
            'handlers': ['demo_file'],
            'level': 'INFO',
        },
    },
}
```

## Verification Checklist

After configuration, verify:

- [ ] `DEMO_MODE` is set in settings.py
- [ ] Middleware is added in correct order
- [ ] Context processor is added to TEMPLATES
- [ ] Demo data file exists: `mnotes/demo_data.py`
- [ ] Management command exists: `mnotes/management/commands/setup_demo_data.py`
- [ ] Run `python manage.py setup_demo_data`
- [ ] Restart Django server
- [ ] Open browser and check for demo banner
- [ ] Try logging in with demo credentials
- [ ] Verify auto-login works
- [ ] Test write operations (should show warnings)

## Configuration Files Summary

| File | Purpose | Required Changes |
|------|---------|------------------|
| `MarketingNotes/settings.py` | Main settings | Add DEMO_MODE, middleware, context processor |
| `mnotes/demo_data.py` | Demo data definitions | Customize demo data (optional) |
| `mnotes/demo_middleware.py` | Auto-login handler | No changes needed |
| `mnotes/context_processors.py` | Template context | No changes needed |
| `toggle_demo_mode.py` | Quick toggle script | No changes needed |

## Common Configuration Scenarios

### Scenario 1: Local Development with Demo
```python
DEBUG = True
DEMO_MODE = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Scenario 2: Client Presentation
```python
DEBUG = False  # For better performance
DEMO_MODE = True
ALLOWED_HOSTS = ['demo.yourdomain.com']
# Use demo credentials provided to client
```

### Scenario 3: Production (No Demo)
```python
DEBUG = False
DEMO_MODE = False  # ⚠️ Critical!
ALLOWED_HOSTS = ['yourdomain.com']
# Use real authentication
```

## Troubleshooting Configuration

### Issue: Demo mode not activating

**Check:**
```python
# 1. Verify setting
print(settings.DEMO_MODE)  # Should print: True

# 2. Check middleware order
# DemoModeMiddleware should be AFTER AuthenticationMiddleware

# 3. Restart server
# Configuration changes require server restart
```

### Issue: Demo banner not showing

**Check:**
```python
# 1. Context processor is added
# Should be in TEMPLATES['OPTIONS']['context_processors']

# 2. Template includes banner
# Add {% include 'mnotes/demo_banner.html' %} to your base template
```

### Issue: Still writing to database in demo mode

**Check:**
```python
# 1. Verify views are updated
# Views should call is_demo_mode()

# 2. Check middleware is active
# DemoModeMiddleware should be in MIDDLEWARE list
```

## Security Best Practices

1. **Never commit demo credentials to version control**
2. **Use environment variables for sensitive settings**
3. **Always disable demo mode in production**
4. **Rotate demo passwords regularly**
5. **Monitor demo mode usage**
6. **Limit demo mode to specific domains**

## Getting Help

If you're having configuration issues:

1. Check the logs: `demo_mode.log`
2. Verify settings: `python manage.py diffsettings`
3. Test middleware: Access any page and check for demo banner
4. Review documentation: `DEMO_MODE_README.md`
5. Contact support or create an issue

---

**Configuration Version**: 1.0  
**Last Updated**: November 7, 2025  
**Django Version**: 3.2+
