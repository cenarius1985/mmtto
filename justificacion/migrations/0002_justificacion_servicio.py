# Generated by Django 2.2.6 on 2019-12-17 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('justificacion', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='justificacion',
            name='servicio',
            field=models.CharField(default='', max_length=255, verbose_name='Unidad/Servicio'),
        ),
    ]
