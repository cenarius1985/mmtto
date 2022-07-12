from django.db import models
import datetime
								

class industriales(models.Model):
    Servicio_Clinico= models.CharField(max_length=100, verbose_name='Servicio/Unidad')
    ##################################################################################
    tipo3 = (
        ('Apoyo Diagnóstico','APOYO DIAGNOSTICO'),('Apoyo Endoscópico','APOYO ENDOSCOPICO'),('Apoyo Industrial','APOYO INDUSTRIAL'),('Apoyo Quirúrgico','APOYO QUIRURGICO')
        ,('Apoyo Terapéutico','APOYO TERAPEUTICO'),('Esterilización','ESTERILIZACION'),('Imagenología','IMAGENOLOGIA'),('Laboratorio/Farmac','LABORATORIO/FARMACIA')
        ,('Med. Fís. Rehabilitación','MED. FIS. REHABILITACION'),('Monitoreo','MONITOREO'),('Odontología','ODONTOLOGIA')
        )
    Clase= models.CharField(max_length=100,choices=tipo3, blank=True, verbose_name='Clase')
    ################################################################################
    tipo4 = (('Alto Costo','ALTO COSTO'),('Mediano Costo','MEDIANO COSTO'),('Bajo Costo','BAJO COSTO'),('Instrumental','INSTRUMENTAL'))
    Subclase= models.CharField(max_length=100, verbose_name='Subclase',choices=tipo4)
    ################################################################################
    Nombre_Equipo= models.CharField(max_length=100, verbose_name='Nombre')
    Marca= models.CharField(max_length=100, verbose_name='Marca')
    Modelo= models.CharField(max_length=100, verbose_name='Modelo')
    Serie = models.CharField(max_length=100, verbose_name='Serie')
    Numero_Inventario= models.CharField(max_length=100, verbose_name='Numero de Inventario', blank=True)
    Valor_Equipo= models.IntegerField(verbose_name='Valor')
    Instalacion=models.DateField(default=datetime.date.today, verbose_name='Instalacion')
    Vida_Util= models.IntegerField(verbose_name='Vida Util')
    ##################################################################################
    tipo = (('Propio','PROPIO'),('Arriendo','ARRIENDO'),('Comodato','COMODATO'))
    Condicion= models.CharField(max_length=10,choices=tipo, blank=True, verbose_name='Condicion')
    ################################################################################
    tipo1 = (('Bueno','BUENO'),('Malo','MALO'),('Regular','REGULAR'),('Baja','BAJA'))
    Estado= models.CharField(max_length=10,choices=tipo1, blank=True, verbose_name='Estado')
    ##################################################################################
    tipo2 = (('Critico','CRITICO'),('Apoyo','APOYO'))
    criticoapoyo= models.CharField(max_length=10,choices=tipo2, blank=True, verbose_name='Critico/Apoyo')
    ##################################################################################
    Frecuencia= models.IntegerField(verbose_name='Frecuencia de MMTTO')
    Responsable= models.CharField(max_length=100, blank=True, verbose_name='Empresa Responsable')
    RUT = models.CharField(max_length=15, blank=True, verbose_name='RUT')
    fechaIG = models.DateField(default=datetime.date.today, verbose_name='Fecha Inicio Garantia')
    fechaTG = models.DateField(default=datetime.date.today, verbose_name='Fecha Termino de la Garantia')
    fechaBaja = models.DateField(default=datetime.date.today, verbose_name='Fecha de Baja', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    
    def __str__ (self):
        return "{0} ({1})".format(self.Nombre_Equipo, self.Numero_Inventario )

    class Meta:
        verbose_name='Inventario de Equipos Industriales'
        ordering = ['-id']