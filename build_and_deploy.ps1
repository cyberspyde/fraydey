#!/usr/bin/env pwsh
# Build and Deploy Static Demo Site

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Fraydey Static Site Builder" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Activate conda environment
Write-Host "Activating environment..." -ForegroundColor Yellow
conda activate fraydey
if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ Failed to activate fraydey environment" -ForegroundColor Red
    exit 1
}

# Collect static files
Write-Host ""
Write-Host "Collecting static files..." -ForegroundColor Yellow
python manage.py collectstatic --noinput --clear

# Build static site
Write-Host ""
Write-Host "Generating static HTML pages..." -ForegroundColor Yellow
python build_static_site.py

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "========================================" -ForegroundColor Green
    Write-Host "✅ BUILD SUCCESSFUL!" -ForegroundColor Green  
    Write-Host "========================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "📂 Static site created in: .\dist" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "🚀 Options to view/deploy:" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Option 1: View locally" -ForegroundColor White
    Write-Host "  cd dist" -ForegroundColor Gray
    Write-Host "  python -m http.server 8000" -ForegroundColor Gray
    Write-Host "  Open: http://localhost:8000" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Option 2: Deploy to Netlify" -ForegroundColor White
    Write-Host "  npm install -g netlify-cli" -ForegroundColor Gray
    Write-Host "  netlify deploy --dir=dist --prod" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Option 3: Deploy to Vercel" -ForegroundColor White
    Write-Host "  npm install -g vercel" -ForegroundColor Gray
    Write-Host "  cd dist && vercel --prod" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Option 4: Upload to any web server" -ForegroundColor White
    Write-Host "  Just upload the 'dist' folder contents" -ForegroundColor Gray
    Write-Host ""
    
    # Ask if user wants to preview
    $preview = Read-Host "Preview site now? (y/n)"
    if ($preview -eq "y" -or $preview -eq "Y") {
        Write-Host ""
        Write-Host "Starting preview server..." -ForegroundColor Yellow
        Set-Location dist
        Write-Host "Opening browser..." -ForegroundColor Yellow
        Start-Sleep -Seconds 2
        Start-Process "http://localhost:8000"
        python -m http.server 8000
    }
} else {
    Write-Host ""
    Write-Host "❌ Build failed. Check errors above." -ForegroundColor Red
}
