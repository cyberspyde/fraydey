# Build Fraydey as Windows Executable
# Run: python build_exe.py

import PyInstaller.__main__
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'manage.py',
    '--name=fraydey-demo',
    '--onefile',
    '--add-data=mnotes;mnotes',
    '--add-data=MarketingNotes;MarketingNotes',
    '--add-data=static;static',
    '--add-data=media;media',
    '--add-data=db.sqlite3;.',
    '--hidden-import=django',
    '--hidden-import=waitress',
    '--hidden-import=PIL',
    '--hidden-import=multiselectfield',
    '--noconsole',
    '--icon=static/images/favicon.ico' if os.path.exists('static/images/favicon.ico') else '',
])
