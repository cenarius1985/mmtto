# Generated by Django 2.2.6 on 2020-06-03 12:27

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordenestalleres', '0002_auto_20200603_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenestalleres',
            name='observaciones',
            field=ckeditor.fields.RichTextField(verbose_name='Observaciones'),
        ),
    ]