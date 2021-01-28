from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test for creating new user"""
        email="test@example.com"
        password="test@12345"
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test for email of new user id normalized"""
        email = "test@EXAMPLE.COM"
        user=get_user_model().objects.create_user(email,'test123')

        self.assertEqual(user.email,email.lower())
    
    def test_new_user_invalid_email(self):
        """creating user with no email user raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'test123')
    
    def test_create_super_user(self):
        """test for creating new super user"""
        user=get_user_model().objects.create_super_user(
            email="test@example.com",
            password="test@12345"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
