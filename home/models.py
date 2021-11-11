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


class Shuttle(Capacity):
    name = models.CharField(null=False, blank=False, max_length=40)


class SpaceStation(Capacity):
    name = models.CharField(null=False, blank=False, max_length=200)


class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, blank=False, on_delete=models.PROTECT)
    offer = models.ForeignKey(Offer, blank=False, null=True, on_delete=models.SET_NULL)
    shuttle = models.ForeignKey(Shuttle, blank=False, null=True, on_delete=models.SET_NULL)
    space_station = models.ForeignKey(SpaceStation, blank=False, null=True, on_delete=models.SET_NULL)
    is_first_class = models.BooleanField(blank=False, default=False, null=False)


class MedicalExamination(models.Model):
    user = models.ForeignKey(CustomUser, blank=False, on_delete=models.PROTECT)
    date = models.DateTimeField(null=True, blank=False)
