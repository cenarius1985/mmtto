# Generated by Django 2.2.6 on 2019-11-07 19:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MantenimientoExterno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField(default=datetime.date.today)),
                ('Unidad', models.CharField(max_length=100, verbose_name='Nombre de la unidad o Centro de Costos')),
                ('Nombre_Equipo', models.CharField(max_length=100, verbose_name='Nombre del equipo o Sistema')),
                ('Marca', models.CharField(max_length=100, verbose_name='Marca')),
                ('Modelo_Equipo', models.CharField(max_length=100, verbose_name='Modelo del Equipo')),
                ('Serie', models.CharField(max_length=100, verbose_name='Numero de Serie')),
                ('Inventario', models.CharField(max_length=100, verbose_name='Numero Inventario')),
                ('Empresa', models.CharField(max_length=100, verbose_name='Nombre de la Empresa')),
                ('Numero', models.CharField(max_length=100, verbose_name='Numero de Orden de Trabajo')),
                ('Tipo_Mantenimiento', models.CharField(blank=True, choices=[('MP', 'Mantenimiento Preventivo'), ('MC', 'Mantenimiento Correctivo')], default='MP', max_length=2, verbose_name='Mantenimiento Preventivo/Correctivo')),
                ('Critico_Relevante', models.CharField(blank=True, choices=[('CRITICO', 'Critico'), ('RELEVANTE', 'Relevante')], default='RELEVANTE', max_length=10, verbose_name='Critico/Relevante')),
                ('Tecnico', models.CharField(max_length=100, verbose_name='Nombre del Tecnico')),
                ('Horas', models.PositiveSmallIntegerField(verbose_name='Horas Fuera de Servicio')),
                ('Detalle', models.TextField(verbose_name='Detalle')),
                ('Observaciones', models.TextField(verbose_name='Observaciones')),
                ('Fecha_Equipo_Operativo', models.CharField(blank=True, max_length=10, verbose_name='Fecha de Equipo Operativo')),
                ('Fecha_Equipo_Baja', models.CharField(blank=True, max_length=10, verbose_name='Fecha de Baja del Equipo')),
                ('Adjuntar_Archivo', models.FileField(blank=True, upload_to='mantenimiento', verbose_name='Adjuntar Archivo')),
            ],
        ),
    ]
