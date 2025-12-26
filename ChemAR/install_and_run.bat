@echo off
echo ========================================
echo   ChemAR - Interactive Chemistry Lab
echo ========================================
echo.
echo Installing dependencies and starting application...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo Python found! Installing requirements...
pip install -r requirements.txt

if errorlevel 1 (
    echo ERROR: Failed to install requirements
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

echo.
echo Starting ChemAR application...
echo Open your browser to: http://localhost:5000
echo.
echo Press Ctrl+C to stop the application
echo.

python app.py

pause
