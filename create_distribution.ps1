# Create Distribution Package
# This creates a shareable package of your demo

Write-Host "Creating Fraydey Demo Distribution Package..." -ForegroundColor Green
Write-Host ""

# Create dist directory
$distPath = ".\fraydey-demo-package"
if (Test-Path $distPath) {
    Remove-Item $distPath -Recurse -Force
}
New-Item -ItemType Directory -Path $distPath | Out-Null

Write-Host "Copying files..." -ForegroundColor Yellow

# Copy essential files
$excludeItems = @('.git', '__pycache__', '*.pyc', 'dist', 'fraydey-demo-package', '.venv', 'venv', 'node_modules')

Get-ChildItem -Path . | Where-Object {
    $item = $_
    -not ($excludeItems | Where-Object { $item.Name -like $_ })
} | Copy-Item -Destination $distPath -Recurse -Force

Write-Host "Creating README..." -ForegroundColor Yellow

# Create simplified README for distribution
@"
# Fraydey Demo Package

## Quick Start

### Option 1: Windows (Double-click)
1. Double-click **start_demo.bat**
2. Wait for browser to open
3. Login with: demo / demo123

### Option 2: Manual Start
``````bash
# Activate environment
conda activate fraydey

# If first time:
conda create -n fraydey python=3.12
conda activate fraydey
pip install -r requirements.txt
python manage.py migrate
python manage.py setup_demo_data

# Start server
python manage.py runserver 8080
``````

Then open: http://localhost:8080

## Demo Credentials
- **Username**: demo
- **Password**: demo123

## Features
- Pre-populated inventory
- Sales history
- Debt management
- Dashboard with charts
- No data is saved (demo mode)

## Requirements
- Python 3.8+
- Conda or pip

## Support
Visit: https://github.com/cyberspyde/fraydey
"@ | Out-File -FilePath "$distPath\README_DEMO.txt" -Encoding UTF8

Write-Host "Creating archive..." -ForegroundColor Yellow

# Create ZIP file
$zipPath = ".\fraydey-demo-v1.0.zip"
if (Test-Path $zipPath) {
    Remove-Item $zipPath -Force
}

Compress-Archive -Path $distPath -DestinationPath $zipPath -Force

# Cleanup temp folder
Remove-Item $distPath -Recurse -Force

Write-Host ""
Write-Host "✅ SUCCESS!" -ForegroundColor Green
Write-Host ""
Write-Host "Distribution package created: $zipPath" -ForegroundColor Cyan
Write-Host "Size: $([math]::Round((Get-Item $zipPath).Length / 1MB, 2)) MB" -ForegroundColor Cyan
Write-Host ""
Write-Host "Share this file with others!" -ForegroundColor Green
Write-Host "They just need to:" -ForegroundColor Yellow
Write-Host "  1. Unzip the file" -ForegroundColor White
Write-Host "  2. Run start_demo.bat" -ForegroundColor White
Write-Host "  3. Login with demo/demo123" -ForegroundColor White
Write-Host ""
