# Development Quick Start

## For Windows Users

1. Open Command Prompt in the project directory
2. Run: `setup.bat`
3. Once setup is complete, run: `python manage.py runserver`
4. Visit: http://127.0.0.1:8000

## For macOS/Linux Users

1. Open Terminal in the project directory
2. Run: `bash setup.sh`
3. Once setup is complete, run: `python manage.py runserver`
4. Visit: http://127.0.0.1:8000

## Manual Setup (All Platforms)

```bash
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create admin user (optional)
python manage.py createsuperuser

# 6. Create demo data (optional)
python create_demo_data.py

# 7. Start server
python manage.py runserver
```

## Quick Demo Setup

To quickly set up with demo data:

```bash
python create_demo_data.py
```

Then login with:
- Username: demo
- Password: demo123

## Accessing the Application

- **Main App**: http://127.0.0.1:8000
- **Admin Panel**: http://127.0.0.1:8000/admin

## Troubleshooting

See README.md for detailed troubleshooting guide.
