# Generated by Django 2.1 on 2019-10-16 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulancia', '0004_remove_parqueautomotriz_tecnico2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parqueautomotriz',
            name='Movil',
            field=models.CharField(blank=True, default='Ambulancia', max_length=100),
        ),
    ]