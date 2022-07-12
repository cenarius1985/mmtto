from django.db import models
import datetime


class covid(models.Model):
    servicio = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    inventario = models.CharField(max_length=100)
    justificacion = models.CharField(max_length=255, default='S/O', blank=True)
    fecha = models.DateField(default=datetime.date.today)
    tecnico1 = models.CharField(max_length=255, default='Oscar Gonzalez')
    responsable = models.CharField(max_length=255, default='Fernando Ramirez')
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta1 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta2 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta3 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta4 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta5 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta6 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta7 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta8 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta9 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta10 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta11 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta12 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta13 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta14 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta15 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta16 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta17 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta18 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta19 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta20 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta21 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta22 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta23 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta24 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta25 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta26 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta27 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta28 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta29 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta30 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta31 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta32 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta33 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta34 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta35 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta36 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta37 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta38 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta39 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta40 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta41 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta42 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta43 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta44 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta45 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta46 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta47 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta48 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta49 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta50 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta51 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta52 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta53 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta54 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta55 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta56 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta57 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta58 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta59 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    SI_NO = (('SI','Si'),('NO','No'),('N/A','N/A'))
    pauta60 = models.CharField(max_length=3,choices=SI_NO, default='SI', blank=True)
####################################################################################
    garantia = models.CharField(max_length=10, default='', blank=True, verbose_name='Numero de Meses en Garantia')
    mantencion = models.CharField(max_length=10, default='', blank=True, verbose_name='Numero de Mantenciones Anuales')
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name='Pautas de Mantenimiento Covid'
        ordering = ['-id']

    def __str__ (self):
        return "{0} ({1})".format(self.servicio, self.inventario )
