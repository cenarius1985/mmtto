from django.db import models
import datetime


class proyectos(models.Model):
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha de Propuesta')
    nombre= models.CharField(max_length=100, verbose_name='Nombre del Proyecto',default='')
    fechaa = models.DateField(default=datetime.date.today, verbose_name='Fecha de Autorizacion (SDA)')
    fechai = models.DateField(default=datetime.date.today, verbose_name='Fecha de Inicio')
    fechat = models.DateField(default=datetime.date.today, verbose_name='Fecha de Termino')
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Proyecto', upload_to='proyectos', blank=True)
    descripcion= models.TextField(verbose_name='Descripcion', blank=True, null=True,default='')
    duracion= models.IntegerField(verbose_name='Duracion (Semanas)')
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    class Meta:
        verbose_name='Propuestas de Proyectos'
        ordering = ['-id']

    def __str__ (self):
        return "{0} ({1})".format(self.nombre, self.fechaa )

