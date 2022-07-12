from django.db import models
import datetime
from ckeditor.fields import RichTextField


class Capacitacion(models.Model):
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha de Emsion')
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Curso')
    modulo = models.CharField(max_length=255, verbose_name='Nombre del Modulo', default='')
    titulo = models.CharField(max_length=255, verbose_name='Nombre Clase', default='')
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Video', upload_to='capacitacion', blank=True)
    Recursos = models.FileField(verbose_name='Adjuntar Recurso', upload_to='capacitacion', blank=True)
    
    def __str__ (self):
        return "{0} ({1})".format(self.fecha, self.nombre )

    class Meta:
        verbose_name='Capacitacion'
        ordering = ['id']
