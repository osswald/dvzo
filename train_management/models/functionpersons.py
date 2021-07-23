from django.db import models

from train_management.models import DvzoFunction
from train_management.models import Personnel


class FunctionPersons(models.Model):
    dvzo_function = models.ForeignKey(DvzoFunction, on_delete=models.CASCADE)
    person = models.ForeignKey(Personnel, on_delete=models.CASCADE)
