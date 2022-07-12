# Generated by Django 2.1 on 2019-10-23 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rrhh',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=100, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=100, verbose_name='Apellidos')),
                ('cargo', models.CharField(max_length=100, verbose_name='Cargo')),
                ('estado', models.CharField(choices=[('Fijo', 'FIJO'), ('Apoyo', 'APOYO')], max_length=100, verbose_name='Fijo/Apoyo')),
                ('unidad', models.CharField(max_length=100, verbose_name='Unidad/Centro Costos')),
                ('funcion', models.CharField(max_length=100, verbose_name='Unidad/Centro Costos')),
                ('contrato', models.CharField(max_length=100, verbose_name='Calidad Contractual')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
        ),
    ]
