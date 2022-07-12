from django.db import models
import datetime


class infraestructura(models.Model):
    sistema= models.CharField(max_length=100, verbose_name='Sistema', blank=True)
    ubicacion= models.CharField(max_length=50, blank=True, verbose_name='Ubicacion')
    frecuencia= models.IntegerField(verbose_name='Frecuencia')
    responsable= models.CharField(max_length=50, blank=True, verbose_name='Responsable')
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.sistema, self.frecuencia )

    class Meta:
        verbose_name='Inventario De Infraestructura'
        ordering = ['-id']