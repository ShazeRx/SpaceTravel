from django.db import models

from home.models import Capacity


class SpaceStation(Capacity):
    name = models.CharField(null=False, blank=False, max_length=200)
