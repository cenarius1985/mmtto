# Generated by Django 2.2.4 on 2019-08-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(default=False, upload_to='Pages', verbose_name='Imagen'),
        ),
    ]
