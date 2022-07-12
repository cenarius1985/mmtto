from django.db import models
import datetime


class Guia(models.Model):
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha de Emsion')
    fecharecepcion = models.DateField(default=datetime.date.today, verbose_name='Fecha de Recepcion')
    nombre = models.CharField(max_length=255, verbose_name='Nombre de la Empresa')
    numero = models.CharField(max_length=255, verbose_name='Numero de guia o Factura',blank=True, null=True)
    monto = models.IntegerField(verbose_name='Monto de la Factura', blank=True, null=True)
####################################################################################
    tipo = (('GUIA','Guia'),('FACTURA','Factura'),('OTRO','Otro'))
    documento = models.CharField(max_length=50,choices=tipo, default='S/I', blank=True)
####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Archivo', upload_to='guia', blank=True)
    
    def __str__ (self):
        return "{0} ({1})".format(self.fecha, self.nombre )

    class Meta:
        verbose_name='Guia'
        ordering = ['-id']