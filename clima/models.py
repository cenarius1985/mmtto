from django.db import models
import datetime


class clima(models.Model):
    servicio= models.CharField(max_length=100, verbose_name='Unidad / Centro de Costos')
    nombre= models.CharField(max_length=100, verbose_name='Nombre del Equipo')
    modelo= models.CharField(max_length=100, verbose_name='Modelo del Equipo')
    marca= models.CharField(max_length=100, verbose_name='Marca del Equipo')
    serie= models.CharField(max_length=100, verbose_name='Numero Serie')
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha de Instalacion')
    responsable= models.CharField(max_length=100, verbose_name='Empresa de MMTTO')
    frecuencia=models.IntegerField(verbose_name='Frecuencia de MMTTO')
################################################################################################################
    Nestado = (('B','Bueno'),('R','Regular'),('M','Malo'),('Baja','BAJA'))
    estado = models.CharField(max_length=5,choices=Nestado, default='B', verbose_name='Condicion del Equipo')
###############################################################################################################
    fecha_baja = models.DateField(default=datetime.date.today,verbose_name='Fecha de Baja', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.servicio, self.serie )

    class Meta:
        verbose_name='Inventario de Equipos de Climatizacion'
        ordering = ['-id']