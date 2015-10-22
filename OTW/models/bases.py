from django.db import models
from django.utils import timezone

from .operario import Operario


class BaseAccion(models.Model):
    descripcion = models.CharField(max_length=128)
    fechafin = models.DateTimeField(null=True)
    fechainicio = models.DateTimeField(default=timezone.now)
    precio = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    unidades = models.DecimalField(default=0, max_digits=8, decimal_places=2)

    class Meta:
        abstract = True
