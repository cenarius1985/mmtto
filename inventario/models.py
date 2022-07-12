from django.db import models
import datetime

# Create your models here.
class inventario(models.Model):
    servicio = models.CharField(max_length=100, verbose_name='Servicio Clinico')
    ##############################################################################
    tipo3 = (
        ('Apoyo Diagnóstico','APOYO DIAGNOSTICO'),('Apoyo Endoscópico','APOYO ENDOSCOPICO'),('Apoyo Industrial','APOYO INDUSTRIAL'),('Apoyo Quirúrgico','APOYO QUIRURGICO')
        ,('Apoyo Terapéutico','APOYO TERAPEUTICO'),('Esterilización','ESTERILIZACION'),('Imagenología','IMAGENOLOGIA'),('Laboratorio/Farmac','LABORATORIO/FARMACIA')
        ,('Med. Fís. Rehabilitación','MED. FIS. REHABILITACION'),('Monitoreo','MONITOREO'),('Odontología','ODONTOLOGIA'),('Instrumental','INSTRUMENTAL')
        )
    clase = models.CharField(max_length=100, verbose_name='Clase',choices=tipo3)
    ##############################################################################
    tipo4 = (('Alto Costo','ALTO COSTO'),('Mediano Costo','MEDIANO COSTO'),('Bajo Costo','BAJO COSTO'))
    subclase = models.CharField(max_length=100, verbose_name='Subclase',choices=tipo4)
    ##############################################################################
    nombre_equipo = models.CharField(max_length=100,verbose_name='Nombre del Equipo')
    marca = models.CharField(max_length=100, verbose_name='Marca')
    modelo = models.CharField(max_length=100, verbose_name='Modelo')
    serie = models.CharField(max_length=100, verbose_name='Numero de Serie')
    inventario = models.CharField(max_length=100, verbose_name='Numero Inventario')
    licitacion = models.CharField(max_length=100, verbose_name='Numero de Licitacion', blank=True)
    valor = models.CharField(max_length=100, verbose_name='Valor el Equipo')
    fecha= models.DateField(default=datetime.date.today,verbose_name='Fecha de Instalacion')
    vida_util= models.IntegerField(verbose_name='Vida Util')
    ano=models.IntegerField(verbose_name='Año de Instalacion')
######################################################################################
    Econtrato = (('ARRIENDO','Arriendo'),('COMODATO','Comodato'),('PROPIO','Propio'))
    contrato = models.CharField(max_length=10,choices=Econtrato, default='PROPIO', verbose_name='Tipo de Contrato')
######################################################################################
    Nestado = (('B','Bueno'),('R','Regular'),('M','Malo'),('Baja','BAJA'))
    estado = models.CharField(max_length=5,choices=Nestado, default='B', verbose_name='Condicion del Equipo')
######################################################################################   
    tipo = (('C','Critico'),('A','Apoyo'))
    critico_apoyo = models.CharField(max_length=1,choices= tipo, default='A', verbose_name='Critico/Apoyo')
######################################################################################      
    frecuencia = models.IntegerField(verbose_name='Frecuencia de Mantenimiento')
    empresa = models.CharField(max_length=100, verbose_name='Nombre de la Empresa')
    rut = models.CharField(max_length=15, verbose_name='RUT de la Empresa')
    garantia_inicio = models.DateField(default=datetime.date.today,verbose_name='Fecha de Inicio de la Garantia')
    garantia_final = models.DateField(default=datetime.date.today,verbose_name='Fecha de Inicio de Termino')
    fecha_baja = models.DateField(default=datetime.date.today,verbose_name='Fecha de Baja', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Archivo', upload_to='inventario', blank=True)
    def __str__(self):
        return "{0} ({1})".format(self.nombre_equipo, self.inventario)

    class Meta:
        verbose_name='Inventario'
        ordering = ['-id']