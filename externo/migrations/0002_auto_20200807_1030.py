# Generated by Django 3.0.7 on 2020-08-07 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('externo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mantenimientoexterno',
            options={'ordering': ['-id'], 'verbose_name': 'Mantenimiento Externo'},
        ),
        migrations.AlterField(
            model_name='mantenimientoexterno',
            name='Fecha_Equipo_Operativo',
            field=models.CharField(blank=True, default='', max_length=10, verbose_name='Fecha de Equipo Operativo'),
        ),
    ]