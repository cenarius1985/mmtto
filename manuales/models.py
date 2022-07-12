from django.db import models
import datetime


class Manuales(models.Model):
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha de Emsion')
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Documento')
    marca = models.CharField(max_length=255, verbose_name='Marca', default='')
    modelo = models.CharField(max_length=255, verbose_name='Modelo', default='')
    representante = models.CharField(max_length=255, verbose_name='Representante de la Marca', default='')
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Archivo', upload_to='manuales', blank=True)
    
    def __str__ (self):
        return "{0} ({1})".format(self.fecha, self.nombre )

    class Meta:
        verbose_name='Manuales'
        ordering = ['-id']