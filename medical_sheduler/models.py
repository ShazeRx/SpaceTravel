from django.db import models

from authentication.models import CustomUser


class MedicalExamination(models.Model):
    user = models.ForeignKey(CustomUser, blank=False, on_delete=models.PROTECT)
    date = models.DateTimeField(null=True, blank=False)
