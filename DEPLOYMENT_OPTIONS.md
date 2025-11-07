# Fraydey Demo Deployment Guide

## 🚀 Deployment Options for Demo Site

Since Fraydey is a Django application, it cannot be converted to a pure static site. 
However, here are the best options to share your demo:

---

## Option 1: **Docker (Recommended for Portability)**

### Prerequisites:
- Install Docker Desktop for Windows

### Build and Run:
```bash
# Build the Docker image
docker-compose build

# Start the container
docker-compose up

# Access at: http://localhost:8080
```

### Share Docker Image:
```bash
# Save image to file
docker save fraydey:demo > fraydey-demo.tar

# Others can load it:
docker load < fraydey-demo.tar
docker run -p 8080:8080 fraydey:demo
```

---

## Option 2: **Deploy to Render.com (Free Tier)**

1. Create account at https://render.com
2. Create new "Web Service"
3. Connect your GitHub repo
4. Use these settings:
   - **Build Command**: `pip install -r requirements.txt && python manage.py migrate && python manage.py setup_demo_data`
   - **Start Command**: `python manage.py runserver 0.0.0.0:8080`
   - **Environment Variables**: 
     - `DEMO_MODE=True`
     - `SECRET_KEY=your-secret-key`

**Result**: Live demo URL like `https://fraydey-demo.onrender.com`

---

## Option 3: **Deploy to PythonAnywhere (Free Tier)**

1. Sign up at https://www.pythonanywhere.com
2. Upload your code
3. Set up virtual environment
4. Configure WSGI file
5. Enable demo mode

**Result**: Live URL like `https://yourusername.pythonanywhere.com`

---

## Option 4: **Deploy to Heroku**

Create `Procfile`:
```
web: python manage.py runserver 0.0.0.0:$PORT
```

Deploy:
```bash
heroku create fraydey-demo
heroku config:set DEMO_MODE=True
git push heroku main
```

---

## Option 5: **Capture Static HTML Snapshots** (Limited Functionality)

### Using wget (Windows):
```powershell
# Install: choco install wget
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent http://localhost:8080 -P ./dist
```

### Using HTTrack (GUI):
1. Download HTTrack from https://www.httrack.com/
2. Enter URL: http://localhost:8080
3. Save to ./dist folder
4. Open ./dist/index.html in browser

⚠️ **Warning**: Static HTML loses all functionality:
- No login
- No database interactions
- No form submissions
- Only visual demonstration

---

## Option 6: **Windows Executable (Advanced)**

### Build with PyInstaller:
```powershell
pip install pyinstaller
python build_exe.py
```

Creates `fraydey-demo.exe` that others can run directly.

⚠️ **Note**: Large file size (~100MB+), Windows only

---

## Option 7: **ZIP and Share (Simplest)**

### Package for sharing:
```powershell
# Create dist folder
mkdir dist
Copy-Item -Path . -Destination ./dist/fraydey -Recurse -Exclude @('.git', '__pycache__', '*.pyc', 'dist')

# Create run script
@"
@echo off
echo Starting Fraydey Demo...
cd fraydey
call conda activate fraydey
if errorlevel 1 (
    echo Creating conda environment...
    conda create -n fraydey python=3.12 -y
    conda activate fraydey
    pip install -r requirements.txt
)
python manage.py migrate
python manage.py setup_demo_data
python manage.py runserver 8080
pause
"@ | Out-File -FilePath ./dist/run_demo.bat -Encoding ASCII

# Compress
Compress-Archive -Path ./dist -DestinationPath fraydey-demo.zip
```

**Share**: Send `fraydey-demo.zip` - users run `run_demo.bat`

---

## Recommended Approach by Use Case:

| Use Case | Best Option | Reason |
|----------|-------------|--------|
| **Quick sharing** | ZIP + BAT file | No setup needed |
| **Online demo** | Render.com | Free, easy, live URL |
| **Client presentation** | Docker | Professional, portable |
| **Screenshots only** | HTTrack | Static HTML works |
| **Trade show (offline)** | Windows .exe | No internet needed |

---

## Quick Setup for Current Demo:

**For immediate online deployment to Render.com:**

```bash
# 1. Push to GitHub (if not already)
git add .
git commit -m "Add demo mode"
git push

# 2. Go to render.com and create web service
# 3. Connect GitHub repo
# 4. Done! Live in 5 minutes
```

---

## Support

Choose the option that best fits your needs. For most cases, I recommend:
- **Render.com** (for online demos)
- **Docker** (for sharing with technical users)
- **ZIP + BAT** (for sharing with non-technical users)
