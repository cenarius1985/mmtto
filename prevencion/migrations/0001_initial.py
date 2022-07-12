# Generated by Django 3.0.4 on 2020-06-18 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prevencion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(default=datetime.date.today, verbose_name='Fecha de Emsion')),
                ('fecharecepcion', models.DateField(default=datetime.date.today, verbose_name='Fecha de Recepcion')),
                ('desde', models.CharField(blank=True, default='', max_length=255, verbose_name='Desde')),
                ('hacia', models.CharField(blank=True, default='', max_length=255, verbose_name='Hacia')),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre del Documento')),
                ('documento', models.CharField(blank=True, choices=[('MEMO', 'Memo'), ('INFORME', 'Informe'), ('ORDINARIO', 'Ordinario'), ('RESOLUCION', 'Resolucion'), ('OTRO', 'Otro')], default='S/I', max_length=50)),
                ('recepcion', models.CharField(default='', max_length=255, verbose_name='Recepcionado Por:')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('Adjuntar_Archivo', models.FileField(blank=True, upload_to='control', verbose_name='Adjuntar Archivo')),
            ],
            options={
                'verbose_name': 'Prevencion',
                'ordering': ['-id'],
            },
        ),
    ]
