from django.db import models
import datetime


class roperiaconfeccion(models.Model):	

    Fecha_OC= models.DateField(default=datetime.date.today, verbose_name='Fecha Orden Compra')
    Numero_Boleta = models.CharField(max_length=100, verbose_name='Numero Boleta')
    RUT = models.CharField(max_length=25, verbose_name='RUT')
    Nombre_Empresa = models.CharField(max_length=100, verbose_name='Nombre de Empresa')
    Detalle = models.CharField(max_length=100, verbose_name='Descripcion del Servicio')
    Valor = models.IntegerField(verbose_name='Valor')
    OC = models.CharField(max_length=100, verbose_name='N° Orden de Compra')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.Fecha_OC, self.Numero_Boleta )

    class Meta:
        verbose_name='Boleta Confeccion de Ropa'
        ordering = ['-id']