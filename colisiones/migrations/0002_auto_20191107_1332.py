# Generated by Django 2.2.6 on 2019-11-07 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colisiones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='colisiones',
            name='colision',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Hora de Colision'),
        ),
        migrations.AlterField(
            model_name='colisiones',
            name='salida',
            field=models.CharField(max_length=100, verbose_name='Hora de Salida'),
        ),
    ]
