# Expenses tests
from django.test import TestCase, Client
from django.contrib.auth.models import User
from expenses.models import Expense
from accounts.models import StudentProfile
from decimal import Decimal


class ExpenseModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.profile = StudentProfile.objects.create(user=self.user, monthly_budget=Decimal('500.00'))
    
    def test_create_expense(self):
        expense = Expense.objects.create(
            user=self.user,
            title='Test Expense',
            amount=Decimal('25.00'),
            category='food',
            date='2024-03-31'
        )
        self.assertEqual(expense.title, 'Test Expense')
        self.assertEqual(expense.amount, Decimal('25.00'))
    
    def test_expense_str(self):
        expense = Expense.objects.create(
            user=self.user,
            title='Lunch',
            amount=Decimal('12.50'),
            category='food',
            date='2024-03-31'
        )
        self.assertEqual(str(expense), 'Lunch - 12.50 (Food)')


class ExpenseViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
        self.profile = StudentProfile.objects.create(user=self.user, monthly_budget=Decimal('500.00'))
    
    def test_expense_list_requires_login(self):
        response = self.client.get('/expenses/')
        self.assertEqual(response.status_code, 302)  # Redirect to login
    
    def test_expense_list_logged_in(self):
        self.client.login(username='testuser', password='password')
        response = self.client.get('/expenses/')
        self.assertEqual(response.status_code, 200)
