# Generated by Django 3.0.7 on 2020-06-26 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guia', '0003_auto_20200626_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='guia',
            name='numero',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Numero de guia o Factura'),
        ),
    ]
