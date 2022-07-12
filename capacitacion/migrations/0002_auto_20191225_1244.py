# Generated by Django 2.2.6 on 2019-12-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacitacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='capacitacion',
            options={'ordering': ['id'], 'verbose_name': 'Capacitacion'},
        ),
        migrations.RemoveField(
            model_name='capacitacion',
            name='servicio',
        ),
        migrations.AddField(
            model_name='capacitacion',
            name='titulo',
            field=models.CharField(default='', max_length=255, verbose_name='Nombre Clase'),
        ),
        migrations.AlterField(
            model_name='capacitacion',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='CURSO'),
        ),
    ]
