# Generated by Django 2.1 on 2019-10-24 14:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clima',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servicio', models.CharField(max_length=100, verbose_name='Unidad / Centro de Costos')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del Equipo')),
                ('modelo', models.CharField(max_length=100, verbose_name='Modelo del Equipo')),
                ('marca', models.CharField(max_length=100, verbose_name='Marca del Equipo')),
                ('serie', models.CharField(max_length=100, verbose_name='Numero Serie')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha de Instalacion')),
                ('responsable', models.CharField(max_length=100, verbose_name='Empresa de MMTTO')),
                ('frecuencia', models.IntegerField(verbose_name='Frecuencia de MMTTO')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
    ]
