# Generated by Django 2.1 on 2019-10-25 13:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='roperiaconfeccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_OC', models.DateField(default=datetime.date.today, verbose_name='Fecha Orden Compra')),
                ('Numero_Boleta', models.CharField(max_length=100, verbose_name='Numero Boleta')),
                ('RUT', models.CharField(max_length=25, verbose_name='RUT')),
                ('Nombre_Empresa', models.CharField(max_length=100, verbose_name='Nombre de Empresa')),
                ('Detalle', models.CharField(max_length=100, verbose_name='Descripcion del Servicio')),
                ('Valor', models.IntegerField(verbose_name='Valor')),
                ('OC', models.CharField(max_length=100, verbose_name='N° Orden de Compra')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
    ]
