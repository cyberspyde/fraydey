@echo off
echo ========================================
echo Fraydey Demo Mode - Quick Start
echo ========================================
echo.

REM Check if conda is available
where conda >nul 2>nul
if %errorlevel% neq 0 (
    echo ERROR: Conda not found. Please install Anaconda or Miniconda first.
    pause
    exit /b 1
)

echo Activating fraydey environment...
call conda activate fraydey
if %errorlevel% neq 0 (
    echo Creating fraydey conda environment...
    call conda create -n fraydey python=3.12 -y
    call conda activate fraydey
    
    echo Installing dependencies...
    pip install -r requirements.txt
    
    echo Setting up database...
    python manage.py migrate
    
    echo Creating demo data...
    python manage.py setup_demo_data
)

echo.
echo ========================================
echo Starting Fraydey Demo Server...
echo ========================================
echo.
echo Demo Credentials:
echo   Username: demo
echo   Password: demo123
echo.
echo Opening browser in 3 seconds...
echo Press Ctrl+C to stop the server
echo ========================================
echo.

REM Wait 3 seconds then open browser
timeout /t 3 /nobreak >nul
start http://localhost:8080

REM Start the server
python manage.py runserver 8080

pause
