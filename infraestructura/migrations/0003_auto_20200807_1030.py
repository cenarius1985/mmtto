# Generated by Django 3.0.7 on 2020-08-07 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('infraestructura', '0002_auto_20191022_1355'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='infraestructura',
            options={'ordering': ['-id'], 'verbose_name': 'Inventario De Infraestructura'},
        ),
    ]