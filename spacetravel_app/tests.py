from django.contrib.auth import get_user_model
from unittest import TestCase
import pytest


class CustomUserManagerTests(TestCase):

    @pytest.mark.django_db
    def test_should_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='test@example.com', password='fizz', date_of_birth='1999-06-29')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

    @pytest.mark.django_db
    def test_should_raise_type_error_when_empty_or_wrong_fields(self):
        User = get_user_model()
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='fizz', date_of_birth='1999-06-29')
            User.objects.create_user(email='test@example.com', password='', date_of_birth='1999-06-29')
            User.objects.create_user()
            User.objects.create_user(email='test@example.com', password='foo', date_of_birth='')

    @pytest.mark.django_db
    def test_should_create_superuser(self):
        User = get_user_model()
        superuser = User.objects.create_superuser(email='test@example.com', password='fizz')
        self.assertEqual(superuser.email, 'test@example.com')
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
