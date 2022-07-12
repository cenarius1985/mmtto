# Generated by Django 2.2.6 on 2019-11-07 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='colisiones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha de Colision')),
                ('fechasda', models.DateField(default=datetime.date.today, verbose_name='Fecha Informo SDA')),
                ('unidad', models.CharField(blank=True, choices=[('Samu', 'SAMU'), ('Urgencia', 'URGENCIA'), ('ssgg', 'SSGG')], default='SSGG', max_length=10, verbose_name='Servicio')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre y Apellido del Conductor')),
                ('patente', models.CharField(max_length=100, verbose_name='Patente Movil')),
                ('valor', models.CharField(max_length=100, verbose_name='Valor de los Daños')),
                ('salida', models.CharField(max_length=100, verbose_name='Horario de Salida')),
                ('inicio', models.CharField(max_length=100, verbose_name='Direccion Salida')),
                ('final', models.CharField(max_length=100, verbose_name='Direccion Final')),
                ('kilometraje', models.CharField(max_length=100, verbose_name='Kilometraje')),
                ('numeromotor', models.CharField(max_length=100, verbose_name='Numero de Motor')),
                ('numerochasis', models.CharField(max_length=100, verbose_name='Numero de Chasis')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('Adjuntar_Archivo', models.FileField(blank=True, upload_to='colisiones', verbose_name='Adjuntar Archivo')),
            ],
        ),
    ]
