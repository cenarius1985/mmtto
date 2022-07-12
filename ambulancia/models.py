from django.db import models
import datetime


class ParqueAutomotriz(models.Model):
    Movil= models.CharField(max_length=100, blank=True, default='Ambulancia')
    Patente = models.CharField(max_length=100, blank=True)
    marca = models.CharField(max_length=100, blank=True, default='Mercedes Benz')
    Servicio = models.CharField(max_length=100, blank=True)
    modelo = models.CharField(max_length=100, blank=True)
    inventario = models.CharField(max_length=100, blank=True)
    observacion = models.TextField()
    fecha = models.DateField(default=datetime.date.today)
    tecnico1 = models.CharField(max_length=255, blank=True)
    responsable = models.CharField(max_length=255, blank=True)
    km_anterior = models.CharField(max_length=100, blank=True)
    proximo_cambio = models.CharField(max_length=100, blank=True)
    km_programado = models.CharField(max_length=100 , blank=True)
    km_real = models.CharField(max_length=100, blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta1 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta2 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta3 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta4 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta5 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta6 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta7 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta8 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta9 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta10 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta11 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta12 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta13 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta14 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta15 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta16 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta17 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'))
    pauta18 = models.CharField(max_length=2,choices=SI_NO, default='SI', blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name='Parque Automotriz'
        ordering = ['-id']

    def __str__ (self):
        return "{0} ({1})".format(self.Servicio, self.Patente )
