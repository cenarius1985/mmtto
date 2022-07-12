from django.db import models
import datetime


class colisiones(models.Model):
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha de Colision')
    fechasda = models.DateField(default=datetime.date.today, verbose_name='Fecha Informo SDA')
    servicio = (('Samu','SAMU'),('Urgencia','URGENCIA'),('ssgg','SSGG'))
    unidad = models.CharField(max_length=10,choices=servicio, default='SSGG', blank=True, verbose_name='Servicio')
    nombre = models.CharField(max_length=255, verbose_name='Nombre y Apellido del Conductor')
    patente= models.CharField(max_length=100, verbose_name='Patente Movil')
    valor = models.CharField(max_length=100,verbose_name='Valor de los Daños')
    salida = models.CharField(max_length=100, verbose_name='Hora de Salida')
    colision = models.CharField(max_length=100, verbose_name='Hora de Colision',blank=True, null=True, default='')
    inicio = models.CharField(max_length=100, verbose_name='Direccion Salida')
    final = models.CharField(max_length=100, verbose_name='Direccion Final')
    kilometraje = models.CharField(max_length=100, verbose_name='Kilometraje')
    numeromotor = models.CharField(max_length=100, verbose_name='Numero de Motor')
    numerochasis = models.CharField(max_length=100, verbose_name='Numero de Chasis')
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Archivo', upload_to='colisiones', blank=True)
    
    def __str__ (self):
        return "{0} ({1})".format(self.patente, self.unidad )

    class Meta:
        verbose_name='Colisiones'
        ordering = ['-id']