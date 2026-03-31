#!/usr/bin/env python
"""
Demo Data Generator for Student Budget Manager
Creates sample users, budgets, and expenses for testing
"""

import os
import sys
import django
from datetime import datetime, timedelta
from decimal import Decimal
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth.models import User
from accounts.models import StudentProfile
from expenses.models import Expense

def create_demo_data():
    """Create sample users and expenses for testing"""
    
    print("\n" + "="*60)
    print("Student Budget Manager - Demo Data Generator")
    print("="*60 + "\n")
    
    # Check if demo user already exists
    if User.objects.filter(username='demo').exists():
        print("⚠️  Demo user already exists. Skipping...")
        return
    
    # Create demo user
    print("[1/3] Creating demo users...")
    demo_user = User.objects.create_user(
        username='demo',
        email='demo@example.com',
        password='demo123',
        first_name='Demo',
        last_name='Student'
    )
    
    # Create student profile with budget
    profile = StudentProfile.objects.create(
        user=demo_user,
        monthly_budget=Decimal('500.00')
    )
    
    print(f"  ✓ Created user: demo (password: demo123)")
    print(f"  ✓ Monthly budget: ${profile.monthly_budget}\n")
    
    # Sample expense data
    print("[2/3] Creating sample expenses...")
    
    categories = ['food', 'transport', 'rent', 'utilities', 'entertainment', 'stationery', 'other']
    expense_titles = {
        'food': ['Coffee', 'Lunch', 'Groceries', 'Pizza', 'Breakfast', 'Dinner', 'Snacks'],
        'transport': ['Uber', 'Gas', 'Metro pass', 'Bus fare', 'Parking', 'Bike repair'],
        'rent': ['Monthly rent', 'Room deposit'],
        'utilities': ['Electricity bill', 'Water bill', 'Internet', 'Phone bill'],
        'entertainment': ['Movie ticket', 'Concert', 'Game', 'Stream subscription', 'Books'],
        'stationery': ['Notebook', 'Pens', 'Printer ink', 'Paper'],
        'other': ['Misc', 'Random', 'Surprise', 'Unexpected']
    }
    
    amounts = {
        'food': [3.5, 8.0, 12.0, 15.0, 5.0],
        'transport': [5.0, 10.0, 25.0, 2.5, 15.0],
        'rent': [250.0, 300.0],
        'utilities': [20.0, 15.0, 25.0, 10.0],
        'entertainment': [12.0, 25.0, 20.0, 10.0, 8.0],
        'stationery': [3.0, 5.0, 8.0, 10.0],
        'other': [7.0, 12.0, 5.0]
    }
    
    # Create expenses for the last 30 days
    expenses_created = 0
    today = datetime.now().date()
    
    for i in range(30):
        # Random number of expenses per day (0-3)
        num_expenses = random.randint(0, 3)
        
        for _ in range(num_expenses):
            category = random.choice(categories)
            title = random.choice(expense_titles[category])
            amount = Decimal(str(random.choice(amounts[category])))
            date = today - timedelta(days=i)
            
            Expense.objects.create(
                user=demo_user,
                title=title,
                amount=amount,
                category=category,
                date=date,
                notes=f"Sample {category} expense"
            )
            expenses_created += 1
    
    print(f"  ✓ Created {expenses_created} sample expenses\n")
    
    # Print summary
    print("[3/3] Summary")
    print("-" * 60)
    
    total_spent = Expense.objects.filter(user=demo_user).aggregate(
        sum=django.db.models.Sum('amount')
    )['sum'] or Decimal('0')
    
    expense_count = Expense.objects.filter(user=demo_user).count()
    
    print(f"  Total expenses: {expense_count}")
    print(f"  Total spent: ${total_spent}")
    print(f"  Budget: ${profile.monthly_budget}")
    print(f"  Remaining: ${profile.monthly_budget - total_spent}")
    print(f"  Usage: {(total_spent/profile.monthly_budget*100):.1f}%")
    
    print("\n" + "="*60)
    print("Demo Data Created Successfully! 🎉")
    print("="*60 + "\n")
    
    print("Login credentials:")
    print("  Username: demo")
    print("  Password: demo123")
    print("\nLogin at: http://127.0.0.1:8000/login/\n")

if __name__ == '__main__':
    try:
        create_demo_data()
    except Exception as e:
        print(f"\n❌ Error: {e}\n")
        sys.exit(1)
