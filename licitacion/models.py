from django.db import models
import datetime


class licitacion(models.Model):
    Nombre= models.CharField(max_length=100, verbose_name='Nombre de Licitacion', blank=True, null=True, default='')
    detalle = models.TextField(verbose_name='Detalle de Licitacion', blank=True, null=True, default='')
    ID_Mercado_Publico= models.CharField(max_length=100, verbose_name='Numero de Licitacion', blank=True, null=True, default='')
    Monto = models.CharField(max_length=100, verbose_name='Monto Asignado', blank=True, null=True, default='')
    Fecha_Publicacion = models.DateField(default=datetime.date.today, verbose_name='Fecha de Publicacion', blank=True, null=True )
    Fecha_Adjudicacion = models.DateField(default=datetime.date.today, verbose_name='Fecha de Adjudicacion', blank=True, null=True)
    ####################################################################################
    estado = (('Abierta','ABIERTA'),('Cerrada','CERRADA'),('Desierta','DESIERTA'),('Adjudicada','ADJUDICADA'),('Revocada','REVOCADA'),('Suspendida','SUSPENDIDA'))
    estadolicitacion= models.CharField(max_length=20,choices=estado, default='', blank=True, verbose_name='Estado de Licitacion')
    ####################################################################################
    adjudicado = models.CharField(max_length=100, verbose_name='Nombre del Adjudicado', blank=True, null=True, default='')
    fechatermino =models.DateField(default=datetime.date.today, verbose_name='Fecha de Termino', blank=True, null=True)
    observaciones=models.TextField(verbose_name='Observaciones', blank=True, null=True, default='')
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.ID_Mercado_Publico, self.Fecha_Publicacion )

    class Meta:
        verbose_name='Licitaciones'
        ordering = ['-id']