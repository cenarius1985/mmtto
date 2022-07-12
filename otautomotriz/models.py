from django.db import models
import datetime


class otautomotriz(models.Model):
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha')
    numeroorden= models.CharField(max_length=100, verbose_name='Numero de OT')
    patente= models.CharField(max_length=10, verbose_name='Patente')
    detalle=models.TextField(verbose_name='Detalle')
    fechaingreso = models.DateField(default=datetime.date.today, verbose_name='Fecha de Ingreso')
    kilometraje= models.IntegerField(verbose_name='Kilometraje Ingreso')
    fechaegreso = models.DateField(default=datetime.date.today, verbose_name='Fecha de Egreso')
    servicio = (('Samu','SAMU'),('Urgencia','URGENCIA'),('Ssgg','SSGG'))
    unidad = models.CharField(max_length=10,choices=servicio, default='SSGG', blank=True, verbose_name='Servicio')
    total = models.IntegerField(verbose_name='Total')
    mantenimiento = (('MP','Mantenimiento Preventivo'),('MC','Mantenimiento Correctivo'))
    tipo_mantenimiento = models.CharField(max_length=2,choices=mantenimiento, default='MP', blank=True, verbose_name="Mantenimiento Preventivo/Correctivo")
    observaciones=models.TextField(verbose_name='Observaciones')
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Archivo', upload_to='automotriz', blank=True)
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.patente, self.kilometraje )

    class Meta:
        verbose_name='Ordene de Trabajo del Parque Automotriz'
        ordering = ['-id']