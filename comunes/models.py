from django.db import models
import datetime


class comunes(models.Model):
    numerofactura= models.CharField(max_length=10, verbose_name='Numero de Factura')
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha')
    primerperiodo = models.DateField(default=datetime.date.today, verbose_name='Periodo de lectura 1°')
    segundoperiodo = models.DateField(default=datetime.date.today, verbose_name='Periodo de lectura 2°')
    fechaemision = models.DateField(default=datetime.date.today, verbose_name='Fecha de Emision')
    watts= models.IntegerField(verbose_name='Consumo (watts/m3)')
    total= models.IntegerField(verbose_name='Total ($)')
    sector= models.CharField(max_length=100, verbose_name='Nombre del Sector')
    direccion= models.CharField(max_length=100, verbose_name='Direccion')
    numeromedidor=models.IntegerField(verbose_name='Numero de Medidor')
    numerocliente=models.IntegerField(verbose_name='Numero de Cliente')
    observaciones=models.TextField(verbose_name='Observaciones')
####################################################################################
    tipo = (('Agua','AGUA'),('Luz','LUZ'),('Internet','INTERNET'),('Gas','GAS'),('Telefonia','TELEFONIA'),('TV Cable','TV CABLE'))
    agualuz= models.CharField(max_length=10,choices=tipo, default='SSGG', blank=True, verbose_name='Servicio')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.agualuz, self.numerofactura )

    class Meta:
        verbose_name='Factura de Gastos Comunes'
        ordering = ['-id']