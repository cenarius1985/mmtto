# Generated by Django 2.2.6 on 2019-11-19 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitoreo', '0012_auto_20191119_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoreo',
            name='responsable',
            field=models.CharField(default='Fernando Ramirez', max_length=255),
        ),
    ]
