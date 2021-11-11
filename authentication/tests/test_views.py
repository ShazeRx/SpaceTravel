from unittest import TestCase

import pytest
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import reverse

from authentication.models import CustomUser


class LoginViewTest(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.user_data = {
            'email': 'test@example.com',
            'password': 'password',
            'date_of_birth': '1999-06-29'
        }
        cls.login_url = reverse("login")
        cls.client = Client()

    def setUp(self) -> None:
        CustomUser.objects.create_user(**self.user_data)

    @pytest.mark.django_db
    def test_should_redirect_on_login_success(self):
        # when
        response = self.client.post(self.login_url, self.user_data, follow=True)
        # then
        self.assertEqual(response.status_code, 200)
        last_url, status_code = response.redirect_chain[-1]
        self.assertEqual(last_url, '/')

    @pytest.mark.django_db
    def test_should_throw_401_on_bad_credentials(self):
        # given
        user_data = self.user_data
        user_data['email'] = 'test@test.pl'
        # when
        response = self.client.post(self.login_url, self.user_data)
        # then
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(response.status_code, 401)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Email or password not correct')
