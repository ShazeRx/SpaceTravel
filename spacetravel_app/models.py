from django.contrib.auth.models import User
from django.db import models


class Offer(models.Model):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)


class Capacity(models.Model):
    capacity = models.IntegerField(null=False, blank=False)

    class Meta:
        abstract = True


class Shuttle(Capacity):
    pass


class SpaceStation(Capacity):
    pass


class Reservation(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.SET_NULL)
    offer = models.ForeignKey(Offer, blank=False, on_delete=models.SET_NULL)
    shuttle = models.ForeignKey(Shuttle, blank=False, on_delete=models.SET_NULL)
    space_station = models.ForeignKey(SpaceStation, blank=False, on_delete=models.SET_NULL)
    is_first_class = models.BooleanField(blank=False, default=False, null=False)


class MedicalExamination(models.Model):
    user = models.ForeignKey(User, blank=False, on_delete=models.SET_NULL)
    date = models.DateTimeField(null=True, blank=False)
