# Generated by Django 2.1 on 2019-10-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulancia', '0005_auto_20191016_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parqueautomotriz',
            name='Patente',
            field=models.CharField(blank=True, default='Mercedez Benz', max_length=100),
        ),
    ]
