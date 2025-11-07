"""
Toggle Demo Mode Script
Run this to quickly enable/disable demo mode
"""

import sys
import os

def toggle_demo_mode(enable=None):
    """Toggle demo mode in settings.py"""
    
    settings_path = 'MarketingNotes/settings.py'
    
    if not os.path.exists(settings_path):
        print("❌ Error: settings.py not found!")
        return
    
    # Read current settings
    with open(settings_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check current state
    if 'DEMO_MODE = True' in content:
        current_state = True
    elif 'DEMO_MODE = False' in content:
        current_state = False
    else:
        print("❌ Error: DEMO_MODE setting not found in settings.py")
        return
    
    # Determine new state
    if enable is None:
        new_state = not current_state
    else:
        new_state = enable
    
    # No change needed
    if new_state == current_state:
        state_text = "enabled" if current_state else "disabled"
        print(f"ℹ️  Demo mode is already {state_text}")
        return
    
    # Update settings
    if new_state:
        content = content.replace('DEMO_MODE = False', 'DEMO_MODE = True')
        print("✅ Demo mode ENABLED")
        print("\n📝 Demo Credentials:")
        print("   Username: demo")
        print("   Password: demo123")
        print("\n⚠️  Remember to run: python manage.py setup_demo_data")
    else:
        content = content.replace('DEMO_MODE = True', 'DEMO_MODE = False')
        print("✅ Demo mode DISABLED")
        print("\n📝 Normal mode restored - database writes are now enabled")
    
    # Write back
    with open(settings_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("\n🔄 Please restart the Django server for changes to take effect")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if arg in ['on', 'enable', 'true', '1']:
            toggle_demo_mode(True)
        elif arg in ['off', 'disable', 'false', '0']:
            toggle_demo_mode(False)
        else:
            print("Usage: python toggle_demo_mode.py [on|off]")
            print("       python toggle_demo_mode.py          (toggles current state)")
    else:
        toggle_demo_mode()
