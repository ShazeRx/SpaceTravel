from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    date_of_birth = models.DateField(blank=False, null=True)
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = CustomUserManager()
