from django.db import models
import datetime


class ropaexterno(models.Model):	

    Nombre_Empresa = models.CharField(max_length=100, verbose_name='Nombre de Empresa')
    Guia = models.CharField(max_length=100, verbose_name='Numero Guia')
    Fecha= models.DateField(default=datetime.date.today, verbose_name='Fecha')
    Detalle = models.CharField(max_length=100, verbose_name='Descripcion')
    Cantidad = models.CharField(max_length=100, verbose_name='Cantidad (Kilos)')
    Precio_Unitario = models.CharField(max_length=100, verbose_name='Precio Unitario')
    Valor = models.IntegerField(verbose_name='Valor')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.Nombre_Empresa, self.Guia)

    class Meta:
        verbose_name='Boleta Confeccion de Ropa'
        ordering = ['-id']