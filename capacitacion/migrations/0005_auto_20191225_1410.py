# Generated by Django 2.2.6 on 2019-12-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0004_auto_20191225_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='capacitacion',
            name='modulo',
            field=models.CharField(default='', max_length=255, verbose_name='Nombre del Modulo'),
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombre del Curso'),
        ),
    ]
