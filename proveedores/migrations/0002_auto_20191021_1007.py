# Generated by Django 2.1 on 2019-10-21 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedores',
            name='numerofactura',
            field=models.CharField(max_length=50, verbose_name='Numero de Factura'),
        ),
        migrations.AlterField(
            model_name='proveedores',
            name='numeroordencompra',
            field=models.CharField(max_length=50, verbose_name='Numero de OC'),
        ),
    ]
