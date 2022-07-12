# Generated by Django 2.1 on 2019-10-18 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssgg', '0005_moviles'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviles',
            name='tipo',
            field=models.CharField(choices=[('Furgon de carga', 'FURGON CARGA'), ('Ambulancia', 'AMBULANCIA'), ('Furgon Pasajeros', 'FURGON PASAJEROS')], default='SSGG', max_length=20, verbose_name='Tipo de Vehiculo'),
        ),
        migrations.AlterField(
            model_name='moviles',
            name='baja',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de Baja'),
        ),
    ]
