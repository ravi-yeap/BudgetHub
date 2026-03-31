@echo off
REM Student Budget Manager - Setup Script for Windows
REM This script helps set up the Django application on Windows

echo.
echo ====================================
echo Student Budget Manager - Setup
echo ====================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://www.python.org/
    pause
    exit /b 1
)

echo [1/5] Creating virtual environment...
if exist venv (
    echo Virtual environment already exists, skipping...
) else (
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment
        pause
        exit /b 1
    )
)

echo [2/5] Activating virtual environment...
call venv\Scripts\activate.bat

echo [3/5] Installing dependencies...
pip install --upgrade pip >nul
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
    pause
    exit /b 1
)

echo [4/5] Running migrations...
python manage.py migrate
if errorlevel 1 (
    echo ERROR: Failed to run migrations
    pause
    exit /b 1
)

echo [5/5] Setup complete!
echo.
echo ====================================
echo Setup Successful!
echo ====================================
echo.
echo To start the development server, run:
echo    python manage.py runserver
echo.
echo Then open your browser to:
echo    http://127.0.0.1:8000
echo.
echo Default test account:
echo    Username: admin (if you created one)
echo.
echo To create an admin account, run:
echo    python manage.py createsuperuser
echo.
pause
