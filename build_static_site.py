"""
Build Static Demo Site
Generates a complete static HTML version of the demo
"""

import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MarketingNotes.settings')
sys.path.insert(0, os.path.dirname(__file__))
django.setup()

from django.core.management import call_command
from django.conf import settings
import shutil

print("=" * 60)
print("Building Static Demo Site for Fraydey")
print("=" * 60)
print()

# Ensure demo mode is enabled
if not getattr(settings, 'DEMO_MODE', False):
    print("⚠️  Warning: DEMO_MODE is not enabled in settings.py")
    print("   Setting DEMO_MODE = True for build...")
    settings.DEMO_MODE = True

# Step 1: Collect static files
print("📦 Step 1: Collecting static files...")
try:
    call_command('collectstatic', '--noinput', '--clear')
    print("✅ Static files collected\n")
except Exception as e:
    print(f"❌ Error collecting static files: {e}\n")

# Step 2: Generate static HTML pages
print("🏗️  Step 2: Generating static HTML pages...")
try:
    call_command('distill-local', '--force', '--exclude-staticfiles')
    print("✅ Static pages generated\n")
except Exception as e:
    print(f"❌ Error generating static pages: {e}")
    print("   Trying alternative method...\n")
    
    # Alternative: Use custom renderer
    from build_static_alternative import build_static_pages
    build_static_pages()

# Step 3: Copy static files to dist
print("📁 Step 3: Copying static files to dist folder...")
dist_dir = settings.DISTILL_DIR
static_src = settings.STATIC_ROOT
static_dest = dist_dir / 'static'

try:
    if static_dest.exists():
        shutil.rmtree(static_dest)
    shutil.copytree(static_src, static_dest)
    print("✅ Static files copied\n")
except Exception as e:
    print(f"⚠️  Warning: {e}\n")

# Step 4: Copy media files (if any)
print("🖼️  Step 4: Copying media files...")
media_src = settings.MEDIA_ROOT
media_dest = dist_dir / 'media'

try:
    if media_dest.exists():
        shutil.rmtree(media_dest)
    if media_src.exists():
        shutil.copytree(media_src, media_dest)
        print("✅ Media files copied\n")
    else:
        print("ℹ️  No media files to copy\n")
except Exception as e:
    print(f"⚠️  Warning: {e}\n")

# Step 5: Create index redirect
print("🔗 Step 5: Creating index redirect...")
index_path = dist_dir / 'index.html'
dashboard_path = dist_dir / 'dashboard' / 'index.html'

if not index_path.exists() and dashboard_path.exists():
    redirect_html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="refresh" content="0; url=./dashboard/">
    <title>Redirecting...</title>
</head>
<body>
    <p>Redirecting to dashboard...</p>
    <p>If not redirected, <a href="./dashboard/">click here</a>.</p>
</body>
</html>"""
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(redirect_html)
    print("✅ Index redirect created\n")

print("=" * 60)
print("✅ BUILD COMPLETE!")
print("=" * 60)
print()
print(f"📂 Output directory: {dist_dir}")
print(f"📊 Generated files:")

# Count generated files
html_count = len(list(dist_dir.rglob('*.html')))
css_count = len(list(dist_dir.rglob('*.css')))
js_count = len(list(dist_dir.rglob('*.js')))
img_count = len(list(dist_dir.rglob('*.png'))) + len(list(dist_dir.rglob('*.jpg'))) + len(list(dist_dir.rglob('*.gif')))

print(f"   - HTML files: {html_count}")
print(f"   - CSS files: {css_count}")
print(f"   - JS files: {js_count}")
print(f"   - Images: {img_count}")
print()
print("🚀 To view the static site:")
print(f"   cd {dist_dir}")
print("   python -m http.server 8000")
print("   Then open: http://localhost:8000")
print()
print("📦 To deploy:")
print("   - Upload the 'dist' folder to any web server")
print("   - Or use: netlify deploy, vercel deploy, etc.")
print()
