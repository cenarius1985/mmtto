# Generated by Django 2.1 on 2019-10-25 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitudestalleresabas', '0002_auto_20191024_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudestalleresabas',
            name='Adjuntar_Archivo',
            field=models.FileField(blank=True, upload_to='inventario', verbose_name='Adjuntar Archivo'),
        ),
        migrations.AlterField(
            model_name='solicitudestalleresabas',
            name='numeroadquisicion',
            field=models.CharField(blank=True, max_length=100, verbose_name='Tipo de Documento'),
        ),
    ]