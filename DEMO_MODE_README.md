# Demo Mode Setup Guide

## Overview

This Django application now includes a **Demo Mode** feature that allows you to showcase the application without requiring database writes. This is perfect for:

- Demonstrating features to potential clients
- Testing the UI/UX without affecting real data
- Providing a sandbox environment for exploration

## Features

✅ **Pre-populated Data**: Demo mode comes with realistic sample data including:
- Demo user account
- Sample products (5 products across different categories)
- Sales history
- Debt records (both buying and selling)
- Vendor information

✅ **No Database Writes**: All POST operations are intercepted and prevented in demo mode

✅ **Auto-Login**: Demo users are automatically logged in

✅ **Visual Indicator**: A prominent banner shows when demo mode is active

## Quick Start

### 1. Enable Demo Mode

Edit `MarketingNotes/settings.py`:

```python
# Demo Mode Configuration
DEMO_MODE = True  # Set to False to disable demo mode
```

### 2. Setup Demo Data (First Time Only)

Run the management command to populate the database with demo data:

```bash
python manage.py setup_demo_data
```

This will create:
- Demo user account
- Sample products
- Sales transactions
- Debt records

### 3. Access Demo Account

**Default Login Credentials:**
- **Username**: `demo`
- **Password**: `demo123`

When `DEMO_MODE = True`, the application will auto-login with these credentials.

## Demo Mode Behavior

### Read Operations
- All views display pre-populated demo data
- Dashboard shows realistic metrics and charts
- Inventory displays sample products
- Sales history is populated

### Write Operations
When a user tries to:
- Create a product
- Edit data
- Delete records
- Sell products
- Pay debts

The system will:
1. Show a warning message: "Bu demo rejim. Ma'lumotlar saqlanmaydi."
2. NOT save any changes to the database
3. Redirect back to the appropriate page

### Visual Indicators

A purple banner appears at the top of all pages showing:
```
🔔 DEMO REJIM | Bu demo versiya - Ma'lumotlar saqlanmaydi | Login: demo | Parol: demo123
```

## Demo Data Details

### Sample Products
1. **Erkaklar ko'ylagi** (Men's Shirt)
   - Initial Price: 150,000 so'm
   - Selling Price: 220,000 so'm
   - Stock: 25 units
   - Sold: 15 units
   - Discount: 10%

2. **Ayollar shim** (Women's Pants)
   - Initial Price: 200,000 so'm
   - Selling Price: 300,000 so'm
   - Stock: 30 units
   - Sold: 22 units

3. **Bolalar kurtka** (Children's Jacket)
   - Initial Price: 180,000 so'm
   - Selling Price: 260,000 so'm
   - Stock: 18 units
   - Sold: 12 units
   - Discount: 15%

4. **Sport futbolka** (Sport T-shirt)
   - Initial Price: 80,000 so'm
   - Selling Price: 130,000 so'm
   - Stock: 50 units
   - Sold: 35 units

5. **Qishki palto** (Winter Coat)
   - Initial Price: 350,000 so'm
   - Selling Price: 520,000 so'm
   - Stock: 12 units
   - Sold: 8 units
   - **On Debt**

### Sales Transactions
- 3 completed sales (fully paid)
- 1 debt sale (partially paid)
- Total revenue displayed on dashboard

### Vendor Information
- Store Name: Demo Fashion Store
- Type: Kiyimlar (Clothing)
- Location: Toshkent, Chilonzor tumani
- Monthly Target: 50,000,000 so'm

## Disabling Demo Mode

To switch back to normal operation:

1. Edit `MarketingNotes/settings.py`:
```python
DEMO_MODE = False
```

2. Restart the Django server

3. The application will now use real database operations

## Technical Details

### Files Added/Modified

**New Files:**
- `mnotes/demo_data.py` - Demo data definitions
- `mnotes/demo_middleware.py` - Middleware for auto-login
- `mnotes/demo_utils.py` - Utility functions for demo mode
- `mnotes/demo_decorators.py` - View decorators
- `mnotes/context_processors.py` - Template context processor
- `mnotes/management/commands/setup_demo_data.py` - Management command
- `mnotes/templates/mnotes/demo_banner.html` - Demo mode banner template

**Modified Files:**
- `MarketingNotes/settings.py` - Added DEMO_MODE setting and middleware
- `mnotes/views.py` - Updated views to support demo mode

### How It Works

1. **Middleware**: `DemoModeMiddleware` checks if demo mode is enabled and handles auto-login
2. **Context Processor**: Makes `DEMO_MODE` available in all templates
3. **View Logic**: Each view checks `is_demo_mode()` and uses demo data instead of database queries
4. **Write Protection**: POST operations are intercepted and display warnings

## Security Notes

⚠️ **Important**: Demo mode is intended for demonstration purposes only.

- **Never enable demo mode in production** with real user data
- Demo credentials are hardcoded and publicly visible
- All users will share the same demo account when enabled
- No authentication is required when demo mode is active

## Customization

### Changing Demo Credentials

Edit `mnotes/demo_data.py`:

```python
DEMO_CREDENTIALS = {
    'username': 'your_demo_username',
    'password': 'your_demo_password',
    'user_id': 1,
}
```

### Adding More Demo Data

Edit the data dictionaries in `mnotes/demo_data.py`:
- `DEMO_PRODUCTS` - Add more products
- `DEMO_SOLD_PRODUCTS` - Add more sales
- `DEMO_BUY_ON_DEBT` - Add more debt records

After modifying, run:
```bash
python manage.py setup_demo_data
```

## Troubleshooting

### Demo mode not working
1. Check `DEMO_MODE = True` in settings.py
2. Verify middleware is added to MIDDLEWARE list
3. Run `setup_demo_data` command
4. Restart Django server

### Data not showing
1. Run: `python manage.py setup_demo_data`
2. Check database has demo user created
3. Verify no errors in console

### Can't login manually
- In demo mode, auto-login is enabled
- To login manually, set `DEMO_MODE = False`

## Support

For issues or questions about demo mode, please refer to the main project documentation or contact the development team.

---

**Created**: November 2025  
**Version**: 1.0  
**Django Version**: 3.2+
