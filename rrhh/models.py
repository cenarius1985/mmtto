from django.db import models
import datetime


class rrhh(models.Model):
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellidos = models.CharField(max_length=100, verbose_name='Apellidos')
    cargo= models.CharField(max_length=100, verbose_name='Cargo')
    aux = (('Fijo','FIJO'),('Apoyo','APOYO'))
    estado = models.CharField(max_length=100,choices=aux, verbose_name='Fijo/Apoyo')
    unidad = models.CharField(max_length=100, verbose_name='Unidad/Centro Costos')
    funcion = models.CharField(max_length=100, verbose_name='Funcion')
    contrato = models.CharField(max_length=100, verbose_name='Calidad Contractual')
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.apellidos, self.cargo )

    class Meta: 
        verbose_name='RRHH'
        ordering = ['-id']