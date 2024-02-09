from django.test import SimpleTestCase, TestCase
from django.urls import reverse
import re
from .models import Profile
from django.contrib.auth.models import User
# Create your tests here.

class ProfilePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        """Tests that template is at correct location"""
        response = self.client.get("/users/profile/", follow=True)
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        """Test url is available by name"""
        response = self.client.get(reverse('profile'), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_template_content(self):
        """Test for the right template name"""
        response = self.client.get(reverse('profile'), follow=True)
        # self.assertTemplateUsed(response, 'users/profile.html')
        pattern = r"Update Profile Information"
        self.assertContains(response, pattern)

class LoginPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        """Tests that template is at correct location"""
        response = self.client.get("/users/login/")
        self.assertEqual(response.status_code, 200)

    def test_url_available_by_name(self):
        """Test url is available by name"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
    def test_correct_template_name(self):
        """Test for the right template name"""
        response = self.client.get(reverse('login'), follow=True)
        self.assertTemplateUsed(response, 'users/login.html')

class LogoutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        """Tests that template is at correct location"""
        response = self.client.get("/users/logout/")
        self.assertEqual(response.status_code, 200)
    def test_url_available_by_name(self):
        """Test url is available by name"""
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)

    def test_correct_template_name(self):
        """Test for the right template name"""
        response = self.client.get(reverse('logout'), follow=True)
        self.assertTemplateUsed(response, 'users/logout.html')

class RegisterPageTests(SimpleTestCase):

    def test_url_exists_at_correct_location(self):
        """Tests that template is at correct location"""
        response = self.client.get("/register/")
        self.assertEqual(response.status_code, 200)
    
    def test_url_available_by_name(self):
        """Test url is available by name"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
    
    def test_template_content(self):
        """Test for the right template name"""
        response = self.client.get(reverse('register'), follow=True)
        # self.assertTemplateUsed(response, 'users/register.html')
        self.assertContains(response, "Join Today")

# Test models

class ProfileModelTest(TestCase):
    """Tests that the Profile model exists"""

    def setUp(self):
        self.user = User(username='Austin', email='austin@cmpny.com')
        self.profile = Profile.objects.create(self.user)

    def test_model_exists(self):
        profiles = Profile.objects.count()

        self.assertEqual(profiles, 0)
    
    def test_model_has_str_representation(self):
        """Test __str__ method """
        self.assertEqual(str(self.profile), self.profile.username + "Profile")