# Accounts tests
from django.test import TestCase, Client
from django.contrib.auth.models import User
from accounts.models import StudentProfile


class StudentProfileTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
    
    def test_profile_created_on_signup(self):
        profile = StudentProfile.objects.get(user=self.user)
        self.assertIsNotNone(profile)
        self.assertEqual(profile.monthly_budget, 0)


class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testuser', 'test@example.com', 'password')
    
    def test_login_page_loads(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
    
    def test_valid_login(self):
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'password'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
    
    def test_invalid_login(self):
        response = self.client.post('/login/', {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Stay on login page
