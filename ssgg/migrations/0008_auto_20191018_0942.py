# Generated by Django 2.1 on 2019-10-18 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ssgg', '0007_auto_20191018_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviles',
            name='numerochasis',
            field=models.CharField(default='Numero de Chasis', max_length=50, verbose_name='Numero de Chasis'),
        ),
        migrations.AlterField(
            model_name='moviles',
            name='numeromotor',
            field=models.CharField(default='Numero de Motor', max_length=50, verbose_name='Numero de Motor'),
        ),
    ]
