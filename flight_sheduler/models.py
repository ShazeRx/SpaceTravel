from django.db import models

from authentication.models import CustomUser
from home.models import Capacity, Offer
from space_station.models import SpaceStation


class Shuttle(Capacity):
    name = models.CharField(null=False, blank=False, max_length=40)


class Reservation(models.Model):
    user = models.ForeignKey(CustomUser, blank=False, on_delete=models.PROTECT)
    offer = models.ForeignKey(Offer, blank=False, null=True, on_delete=models.SET_NULL)
    shuttle = models.ForeignKey(Shuttle, blank=False, null=True, on_delete=models.SET_NULL)
    space_station = models.ForeignKey(SpaceStation, blank=False, null=True, on_delete=models.SET_NULL)
    is_first_class = models.BooleanField(blank=False, default=False, null=False)
