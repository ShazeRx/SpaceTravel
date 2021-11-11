from unittest import TestCase

from authentication.forms import LoginForm


class LoginFormTest(TestCase):

    def test_should_form_be_valid(self):
        user_data = {
            "email": "email@email.com",
            "password": "password"
        }
        form = LoginForm(user_data)
        self.assertTrue(form.is_valid())

    def test_should_form_not_be_valid(self):
        user_data = {
            "email": "emailemail.com",
            "password": "password"
        }
        form = LoginForm(user_data)
        self.assertFalse(form.is_valid())
