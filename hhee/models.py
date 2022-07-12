from django.db import models
import datetime


class hhee(models.Model):
   
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha HHEE')
    nombre= models.CharField(max_length=100, blank=True, verbose_name='Nombre del Funcionario')
    hhee = models.CharField(max_length=100, verbose_name='Horas Realizadas')
    motivo = models.CharField(max_length=255, blank=True, verbose_name='Motivo de HHEE')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.nombre, self.fecha )

    class Meta:
        verbose_name='HHEE'
        ordering = ['-id']