#!/bin/bash

# Student Budget Manager - Setup Script for macOS/Linux
# This script helps set up the Django application

echo ""
echo "===================================="
echo "Student Budget Manager - Setup"
echo "===================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python3 is not installed"
    echo "Please install Python 3.8+ from https://www.python.org/"
    exit 1
fi

echo "[1/5] Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists, skipping..."
else
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment"
        exit 1
    fi
fi

echo "[2/5] Activating virtual environment..."
source venv/bin/activate

echo "[3/5] Installing dependencies..."
pip install --upgrade pip > /dev/null
pip install -r requirements.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies"
    exit 1
fi

echo "[4/5] Running migrations..."
python manage.py migrate
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to run migrations"
    exit 1
fi

echo "[5/5] Setup complete!"
echo ""
echo "===================================="
echo "Setup Successful!"
echo "===================================="
echo ""
echo "To start the development server, run:"
echo "    python manage.py runserver"
echo ""
echo "Then open your browser to:"
echo "    http://127.0.0.1:8000"
echo ""
echo "Default test account:"
echo "    Username: admin (if you created one)"
echo ""
echo "To create an admin account, run:"
echo "    python manage.py createsuperuser"
echo ""
