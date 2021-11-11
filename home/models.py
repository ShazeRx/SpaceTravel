from django.contrib.auth.models import User, AbstractUser
from django.db import models

from authentication.models import CustomUser


class Offer(models.Model):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)


class Capacity(models.Model):
    capacity = models.IntegerField(null=False, blank=False)

    class Meta:
        abstract = True

