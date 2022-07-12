# Generated by Django 2.1 on 2019-10-21 15:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='licitacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=100, verbose_name='Nombre de Licitacion')),
                ('detalle', models.TextField(verbose_name='Detalle de Licitacion')),
                ('ID_Mercado_Publico', models.CharField(max_length=100, verbose_name='Numero de Licitacion')),
                ('Monto', models.CharField(max_length=100, verbose_name='Monto Asignado')),
                ('Fecha_Publicacion', models.DateField(default=datetime.date.today, verbose_name='Fecha de Recepcion')),
                ('Fecha_Adjudicacion', models.DateField(default=datetime.date.today, verbose_name='Fecha de Recepcion')),
                ('estadolicitacion', models.CharField(blank=True, choices=[('Abierta', 'ABIERTA'), ('Cerrada', 'CERRADA'), ('Desierta', 'DESIERTA'), ('Adjudicada', 'ADJUDICADA'), ('REVOCADA', 'Revocada'), ('Suspendida', 'SUSPENDIDA')], default='', max_length=20, verbose_name='Estado de Licitacion')),
                ('adjudicado', models.CharField(max_length=100, verbose_name='Nombre del Adjudicado')),
                ('fechatermino', models.DateField(default=datetime.date.today, verbose_name='Fecha de Termino')),
                ('observaciones', models.TextField(blank=True, default='', null=True, verbose_name='Servicio Prestado')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Licitaciones',
            },
        ),
    ]