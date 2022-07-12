from django.db import models
import datetime

# Create your models here.
class MantenimientoExterno(models.Model):
    Fecha = models.DateField(default=datetime.date.today)
    Unidad = models.CharField(max_length=100, verbose_name="Nombre de la unidad o Centro de Costos")
    Nombre_Equipo = models.CharField(max_length=100, verbose_name="Nombre del equipo o Sistema")
    Marca = models.CharField(max_length=100, verbose_name="Marca")
    Modelo_Equipo = models.CharField(max_length=100,  verbose_name="Modelo del Equipo")
    Serie = models.CharField(max_length=100,  verbose_name="Numero de Serie")
    Inventario = models.CharField(max_length=100,  verbose_name="Numero Inventario")
    Empresa = models.CharField(max_length=100,  verbose_name="Nombre de la Empresa")
    Numero = models.CharField(max_length=100,  verbose_name="Numero de Orden de Trabajo")
####################################################################################
    mantenimiento = (('MP','Mantenimiento Preventivo'),('MC','Mantenimiento Correctivo'))
    Tipo_Mantenimiento = models.CharField(max_length=2,choices=mantenimiento, default='MP', blank=True, verbose_name="Mantenimiento Preventivo/Correctivo")
####################################################################################
    tipo = (('CRITICO','Critico'),('RELEVANTE','Relevante'))
    Critico_Relevante = models.CharField(max_length=10,choices=tipo, default='RELEVANTE', blank=True, verbose_name="Critico/Relevante")
####################################################################################
    Tecnico = models.CharField(max_length=100,  verbose_name="Nombre del Tecnico")
    Horas = models.PositiveSmallIntegerField(verbose_name="Horas Fuera de Servicio")
    Detalle = models.TextField(verbose_name="Detalle")	
    Observaciones = models.TextField(verbose_name="Observaciones")
    Fecha_Equipo_Operativo = models.CharField(max_length=10,  verbose_name="Fecha de Equipo Operativo", blank=True, default='')
    Fecha_Equipo_Baja = models.CharField(max_length=10,  verbose_name="Fecha de Baja del Equipo", blank=True)
####################################################################################
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Archivo', upload_to='mantenimiento', blank=True)

    def __str__ (self):
        return "{0} ({1})".format(self.Nombre_Equipo, self.Numero)
    
    class Meta:
        verbose_name='Mantenimiento Externo'
        ordering = ['-id']