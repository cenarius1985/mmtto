# Generated by Django 2.2.6 on 2019-11-19 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0011_auto_20191119_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoreo',
            name='responsable',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='monitoreo',
            name='tecnico1',
            field=models.CharField(default='Oscar Gonzalez', max_length=255),
        ),
    ]
