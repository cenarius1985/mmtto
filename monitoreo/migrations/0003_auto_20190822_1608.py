# Generated by Django 2.2.4 on 2019-08-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0002_auto_20190821_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoreo',
            name='marca',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='monitoreo',
            name='modelo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='monitoreo',
            name='responsable',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='monitoreo',
            name='tecnico1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='monitoreo',
            name='tecnico2',
            field=models.CharField(max_length=255),
        ),
    ]
