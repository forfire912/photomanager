@echo off
REM Build script for creating Windows executables
REM Usage: build-windows.bat

echo ========================================
echo Photo Manager - Windows Build Script
echo ========================================
echo.

echo [1/4] Installing dependencies...
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo.
echo [2/4] Building CLI executable...
pyinstaller --onefile --name photo-manager-cli photo_manager.py
if errorlevel 1 (
    echo ERROR: Failed to build CLI executable
    pause
    exit /b 1
)

echo.
echo [3/4] Building Web UI executable...
pyinstaller --onefile --name photo-manager-web --add-data "templates;templates" --add-data "static;static" web_ui.py
if errorlevel 1 (
    echo ERROR: Failed to build Web UI executable
    pause
    exit /b 1
)

echo.
echo [4/4] Creating distribution package...
if not exist release mkdir release
copy dist\photo-manager-cli.exe release\
copy dist\photo-manager-web.exe release\
copy README.md release\
copy USAGE_WEB.md release\
copy LICENSE release\

echo.
echo ========================================
echo Build completed successfully!
echo ========================================
echo.
echo Executables created in: dist\
echo Distribution package in: release\
echo.
echo - photo-manager-cli.exe: Command line interface
echo - photo-manager-web.exe: Web interface
echo.
echo To run the web interface:
echo   1. Double-click photo-manager-web.exe
echo   2. Open http://127.0.0.1:5000 in your browser
echo.
pause
