from django.db import models
import datetime


class Control(models.Model):
    fecha = models.DateField(default=datetime.date.today, verbose_name='Fecha de Emsion')
    fecharecepcion = models.DateField(default=datetime.date.today, verbose_name='Fecha de Recepcion')
    desde = models.CharField(max_length=255, verbose_name='Desde', default='', blank=True)
    hacia = models.CharField(max_length=255, verbose_name='Hacia', default='', blank=True)
    nombre = models.CharField(max_length=255, verbose_name='Nombre del Documento')
####################################################################################
    tipo = (('MEMO','Memo'),('INFORME','Informe'),('ORDINARIO','Ordinario'),('RESOLUCION','Resolucion'),('OTRO','Otro'))
    documento = models.CharField(max_length=50,choices=tipo, default='S/I', blank=True)
####################################################################################
    recepcion = models.CharField(max_length=255, verbose_name='Recepcionado Por:', default='')
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Archivo', upload_to='control', blank=True)
    
    def __str__ (self):
        return "{0} ({1})".format(self.fecha, self.nombre )

    class Meta:
        verbose_name='Control'
        ordering = ['-id']