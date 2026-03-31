#!/usr/bin/env python
"""
Quick Start Helper for Student Budget Manager
Helps initialize the application in one command
"""

import os
import sys
import django
from django.conf import settings
from django.core.management import execute_from_command_line

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

def main():
    print("\n" + "="*50)
    print("Student Budget Manager - Quick Start")
    print("="*50 + "\n")
    
    from django.core.management.commands.migrate import Command as MigrateCommand
    from django.core.management.commands.createsuperuser import Command as SuperuserCommand
    
    # Run migrations
    print("[1/2] Running migrations...")
    try:
        execute_from_command_line(['manage.py', 'migrate', '--noinput'])
        print("✓ Migrations completed successfully\n")
    except Exception as e:
        print(f"✗ Error running migrations: {e}\n")
        return False
    
    # Ask if user wants to create superuser
    print("[2/2] Create admin user (optional)?")
    response = input("Create superuser? (y/n): ").lower().strip()
    
    if response == 'y':
        try:
            execute_from_command_line(['manage.py', 'createsuperuser'])
            print("\n✓ Superuser created successfully\n")
        except Exception as e:
            print(f"\n✗ Error creating superuser: {e}\n")
    
    print("="*50)
    print("Setup Complete! 🎉")
    print("="*50)
    print("\nTo start the server, run:")
    print("  python manage.py runserver")
    print("\nThen visit:")
    print("  http://127.0.0.1:8000")
    print("\n")
    
    return True

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)
