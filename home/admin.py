from django.contrib import admin

from home.models import MedicalExamination, Shuttle, SpaceStation, Offer, Reservation, CustomUser

admin.site.register(MedicalExamination)
admin.site.register(Shuttle)
admin.site.register(SpaceStation)
admin.site.register(Offer)
admin.site.register(Reservation)
admin.site.register(CustomUser)
