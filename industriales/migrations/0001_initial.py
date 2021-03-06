# Generated by Django 2.1 on 2019-10-24 17:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='industriales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Servicio_Clinico', models.CharField(max_length=50, verbose_name='Servicio/Unidad')),
                ('Clase', models.CharField(blank=True, choices=[('Apoyo Diagnóstico', 'APOYO DIAGNOSTICO'), ('Apoyo Endoscópico', 'APOYO ENDOSCOPICO'), ('Apoyo Industrial', 'APOYO INDUSTRIAL'), ('Apoyo Quirúrgico', 'APOYO QUIRURGICO'), ('Apoyo Terapéutico', 'APOYO TERAPEUTICO'), ('Esterilización', 'ESTERILIZACION'), ('Imagenología', 'IMAGENOLOGIA'), ('Laboratorio/Farmac', 'LABORATORIO/FARMACIA'), ('Med. Fís. Rehabilitación', 'MED. FIS. REHABILITACION'), ('Monitoreo', 'MONITOREO'), ('Odontología', 'ODONTOLOGIA')], max_length=10, verbose_name='Clase')),
                ('Subclase', models.CharField(choices=[('Alto Costo', 'ALTO COSTO'), ('Mediano Costo', 'MEDIANO COSTO'), ('Bajo Costo', 'BAJO COSTO'), ('Instrumental', 'INSTRUMENTAL')], max_length=50, verbose_name='Subclase')),
                ('Nombre_Equipo', models.CharField(max_length=50, verbose_name='Nombre')),
                ('Marca', models.CharField(max_length=50, verbose_name='Marca')),
                ('Modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('Serie', models.CharField(max_length=50, verbose_name='Serie')),
                ('Numero_Inventario', models.CharField(max_length=50, verbose_name='Numero de Inventario')),
                ('Valor_Equipo', models.IntegerField(verbose_name='Valor')),
                ('Instalacion', models.DateField(default=datetime.date.today, verbose_name='Instalacion')),
                ('Vida_Util', models.IntegerField(verbose_name='Vida Util')),
                ('Condicion', models.CharField(blank=True, choices=[('Propio', 'PROPIO'), ('Arriendo', 'ARRIENDO'), ('Comodato', 'COMODATO')], max_length=10, verbose_name='Condicion')),
                ('Estado', models.CharField(blank=True, choices=[('Bueno', 'BUENO'), ('MALO', 'Malo'), ('Regular', 'REGULAR'), ('Baja', 'BAJA')], max_length=10, verbose_name='Estado')),
                ('criticoapoyo', models.CharField(blank=True, choices=[('Critico', 'CRITICO'), ('Apoyo', 'APOYO')], max_length=10, verbose_name='Estado')),
                ('Frecuencia', models.IntegerField(verbose_name='Frecuencia de MMTTO')),
                ('Responsable', models.CharField(blank=True, max_length=100, verbose_name='Responsable')),
                ('RUT', models.CharField(blank=True, max_length=15, verbose_name='Responsable')),
                ('fechaIG', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('fechaTG', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('fechaBaja', models.DateField(default=datetime.date.today, verbose_name='Fecha')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
    ]
