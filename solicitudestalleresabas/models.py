from django.db import models
import datetime


class solicitudestalleresabas(models.Model):
   
    fecha = models.DateField(default=datetime.date.today, verbose_name='Recepcion MMTTO')
    numeroadquisicion= models.CharField(max_length=100, blank=True, verbose_name='Tipo de Documento')
    ####################################################################################
    estado = (('Pendiente','PENDIENTE'),('Terminada','TERMINADA'),('Abastecimiento','ABASTECIMIENTO'),('SDA','SDA'),('PROCESO','PROCESO'))
    estadoOT= models.CharField(max_length=20,choices=estado, default='', blank=True, verbose_name='Estado de Solicitud')
    ####################################################################################
    tipo = (
        ('66','66-HOSPITALIZACIÓN MEDICINA INTERNA'),('90','90-HOSPITALIZACIÓN QUIRÚRGICA'),('96','96-HOSPITALIZACIÓN UROLOGÍA'),('100','100-HOSPITALIZACIÓN OTORRINOLARINGOLOGÍA'),('111','111-HOSPITALIZACIÓN TRAUMATOLOGÍA'),
        ('113','113-HOSPITALIZACIÓN OBSTETRICIA'),('114','114-HOSPITALIZACIÓN GINECOLOGÍA'),('116','116-HOSPITALIZACIÓN PEDIATRÍA'),('117','117-HOSPITALIZACIÓN NEONATOLOGÍA'),('131','131-HOSPITALIZACIÓN CIRUGÍA PEDIÁTRICA'),
        ('159','159-HOSPITALIZACIÓN DE DIA'),('180','180-UNIDAD DE CUIDADOS INTERMEDIOS ADULTOS'),('195','195-UNIDAD DE TRATAMIENTO INTENSIVO ADULTO'),('205','205-EMERGENCIAS ADULTO'),('215','215-EMERGENCIAS GINECO OBSTÉTRICAS'),
        ('216','216-EMERGENCIAS PEDIÁTRICAS'),('232','232-CONSULTA OTROS PROFESIONALES'),('273','273-CONSULTA MEDICINA INTERNA'),('274','274-CONSULTA NEUROLOGÍA'),('280','280-CONSULTA PSIQUIATRÍA'),
        ('285','285-CONSULTA NEFROLOGÍA'),('290','290-CONSULTA GASTROENTEROLOGÍA'),('294','294-PROGRAMA MANEJO DEL DOLOR'),('295','295-CONSULTA SALUD OCUPACIONAL'),('296','296-CONSULTA ANESTESIA'),
        ('302','302-PROGRAMA ENFERMEDADES DE TRANSMISIÓN SEXUAL'),('309','309-CONSULTA CIRUGÍA GENERAL'),('311','311-CONSULTA UROLOGÍA'),('317','317-CONSULTA OFTALMOLOGÍA'),('319','319-CONSULTA OTORRINOLARINGOLOGÍA'),
        ('321','321-CONSULTA MÉDICA DE TRAUMATOLOGÍA'),('328','328-CONSULTA PEDIATRÍA GENERAL'),('331','331-CONSULTA NEUROLOGÍA PEDIÁTRICA'),('342','342-CONSULTA TRAUMATOLOGÍA PEDIÁTRICA'),('351','351-CONSULTA CIRUGÍA PEDIÁTRICA'),
        ('353','353-CONSULTA GINECOLOGICA'),('354','354-CONSULTA OBSTETRICIA'),('356','356-CONSULTA ODONTOLOGÍA'),('357','357-EMERGENCIAS ODONTOLOGICAS'),('359','359-TELEMEDICINA'),
        ('462','462-QUIRÓFANOS CABEZA Y CUELLO'),('364','364-QUIRÓFANOS CARDIOVASCULAR'),('465','465-QUIRÓFANOS DE EMERGENCIA'),('467','467-QUIRÓFANOS DIGESTIVA'),('470','470-QUIRÓFANOS GINECOLOGÍA'),
        ('476','476-QUIRÓFANOS OBSTETRICIA'),('477','477-QUIRÓFANOS ODONTOLOGICA'),('478','478-QUIRÓFANOS OFTALMOLOGÍA'),('480','480-QUIRÓFANOS OTORRINOLARINGOLOGÍA'),('482','482-QUIRÓFANOS PLÁSTICA'),
        ('485','485-QUIRÓFANOS TRAUMATOLOGÍA Y ORTOPEDIA'),('486','486-QUIRÓFANOS UROLOGÍA'),('493','493-QUIRÓFANOS CIRUGÍA PLÁSTICA'),('240','240-PROCEDIMIENTO DE CARDIOLOGÍA'),('244','244-PROCEDIMIENTO DE NEUMOLOGÍA'),
        ('248','248-PROCEDIMIENTOS DE CARDIOLOGÍA'),('250','250-PROCEDIMIENTOS DE GASTROENTEROLOGÍA'),('251','251-PROCEDIMIENTOS DE GINECOLOGÍA'),('256','256-PROCEDIMIENTOS DE OBSTETRICIA'),('257','257-PROCEDIMIENTOS DE ODONTOLOGÍA'),
        ('258','258-PROCEDIMIENTOS DE OFTALMOLOGÍA'),('261','261-PROCEDIMIENTOS DE OTORRINOLARINGOLOGÍA'),('262','262-PROCEDIMIENTOS DE TRAUMATOLOGÍA'),('263','263-PROCEDIMIENTOS DE UROLOGÍA'),('267','267-PROCEDIMIENTOS ENDOSCÓPICOS'),
        ('471','471-QUIRÓFANOS MAYOR AMBULATORIA'),('517','517-SALAS DE PARTO'),('518','518-LABORATORIO CLÍNICO'),('531','531-TOMA DE MUESTRA'),('540','540-MAMOGRAFÍA'),
        ('541','541-TOMOGRAFÍA'),('542','542-IMAGENOLOGÍA'),('544','544-ANATOMÍA PATOLÓGICA'),('567','567-REHABILITACIÓN'),('593','593-SERVICIO FARMACEUTICO'),
        ('644','644-AMBULANCIA'),('648','648-ASEO'),('652','652-SERVICIO DE ALIMENTACIÓN'),('657','657-LAVANDERIA Y ROPERIA'),
        ('644','644-TRANSPORTE GENERAL'),('713','713-TRABAJO SOCIAL'),('670','670-ADMINISTRACIÓN'),('567','567-REHABILITACIÓN'),('662','662-ESTERILIZACIÓN'),
        ('152','152-HOSPITALIZACIÓN EN CASA'),('530','530-LABORATORIO DE BIOLOGÍA MOLECULAR'),)
    servicioorigen= models.CharField(max_length=50,choices=tipo, blank=True, verbose_name='Servicio que Solicita')
    ####################################################################################
    fechasda = models.DateField(default=datetime.date.today, verbose_name='Fecha SDA', blank=True, null=True)
    fechaabast = models.DateField(default=datetime.date.today, verbose_name='Fecha Abastecimiento',blank=True, null=True)
    fecha_OrdenCompra = models.DateField(default=datetime.date.today, verbose_name='Emsion OC', blank=True, null=True)
    fecha_Factura = models.DateField(default=datetime.date.today, verbose_name='E. Factura', blank=True, null=True)
    detalle=models.TextField(verbose_name='Detalle')
    observaciones=models.TextField(verbose_name='Observaciones')
    ####################################################################################
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    Adjuntar_Archivo = models.FileField(verbose_name='Adjuntar Archivo', upload_to='abastecimiento', blank=True)
    
    def __str__ (self):
        return "{0} ({1})".format(self.numeroadquisicion, self.estadoOT )

    class Meta:
        verbose_name='Solicitudes de Abastecimiento'
        ordering = ['-id']