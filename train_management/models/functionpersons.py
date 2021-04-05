from django.db import models

from train_management.models import DvzoFunction, Personnel


class FunctionPersons(models.Model):
    dvzo_function = models.ForeignKey(DvzoFunction, on_delete=models.DO_NOTHING)
    person = models.ForeignKey(Personnel, on_delete=models.DO_NOTHING)
