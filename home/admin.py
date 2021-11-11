from django.contrib import admin

from authentication.models import CustomUser
from flight_sheduler.models import Shuttle, Reservation
from home.models import Offer
from medical_sheduler.models import MedicalExamination
from space_station.models import SpaceStation

admin.site.register(MedicalExamination)
admin.site.register(Shuttle)
admin.site.register(SpaceStation)
admin.site.register(Offer)
admin.site.register(Reservation)
admin.site.register(CustomUser)
