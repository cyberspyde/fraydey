# Quick Start Guide - Demo Mode Setup

## Prerequisites
- Python 3.8+ installed
- Django 3.2+ installed
- Git (optional, for cloning)

## Step-by-Step Setup

### 1. Install Dependencies

Make sure you're in the project directory:

```bash
cd fraydey
```

Install required packages:

```bash
pip install django django_resized django_multiselectfield pillow
```

Or use requirements.txt:

```bash
pip install -r requirements.txt
```

### 2. Enable Demo Mode

**Option A: Using the toggle script (Recommended)**

```bash
python toggle_demo_mode.py on
```

**Option B: Manual configuration**

Edit `MarketingNotes/settings.py` and set:

```python
DEMO_MODE = True
```

### 3. Setup Database and Demo Data

Run migrations:

```bash
python manage.py migrate
```

Create demo data:

```bash
python manage.py setup_demo_data
```

Expected output:
```
Setting up demo data...
Created demo user: demo
Created demo profile
Created demo vendor
Created product: Erkaklar ko'ylagi
Created product: Ayollar shim
...
=== Demo data setup complete! ===
Username: demo
Password: demo123
```

### 4. Start the Development Server

```bash
python manage.py runserver
```

### 5. Access the Application

Open your browser and go to:
```
http://localhost:8000
```

You should be automatically logged in with the demo account!

## Verifying Demo Mode

You should see:
1. ✅ A purple banner at the top: "DEMO REJIM"
2. ✅ Pre-populated inventory with 5 products
3. ✅ Dashboard with sales data and charts
4. ✅ When you try to create/edit/delete, you'll see a warning message

## Switching to Normal Mode

When you're ready to use the application normally:

```bash
python toggle_demo_mode.py off
```

Or manually edit `settings.py`:
```python
DEMO_MODE = False
```

Then restart the server:
```bash
# Press Ctrl+C to stop the server
python manage.py runserver
```

## Creating Your Own Account (Normal Mode)

With demo mode OFF:

1. Go to: http://localhost:8000
2. Click "Ro'yxatdan o'tish" (Register)
3. Choose "Savdogar" (Vendor)
4. Fill in your details
5. Login with your credentials

## Troubleshooting

### Issue: "Module not found" errors

**Solution:** Install missing dependencies
```bash
pip install django django_resized django_multiselectfield pillow
```

### Issue: Demo data not showing

**Solution:** Run setup command again
```bash
python manage.py setup_demo_data
```

### Issue: Server won't start

**Solution:** Check if port 8000 is available
```bash
# Try a different port
python manage.py runserver 8001
```

### Issue: Changes in demo mode are being saved

**Solution:** Verify demo mode is enabled
```bash
# Check settings.py has:
DEMO_MODE = True

# Restart server after changing
```

### Issue: Can't login with demo credentials

**Solution:** Make sure demo data was created
```bash
python manage.py setup_demo_data
```

## Next Steps

- 📖 Read [DEMO_MODE_README.md](DEMO_MODE_README.md) for detailed documentation
- 🎨 Customize demo data in `mnotes/demo_data.py`
- 🚀 Deploy to production (remember to disable demo mode!)
- 💬 Join the community - report issues or contribute

## Support

Need help? 
- Create an issue on GitHub
- Contact: cyberspyde@gmail.com
- Telegram: @cyberspyde_admin

---

**Happy Demo-ing! 🎉**
