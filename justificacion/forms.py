from django.forms import ModelForm
from django import forms
from .models import Justificacion


class JustificacionForm(ModelForm):
    class Meta:
        model = Justificacion
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Informe de Justificacion'}),
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad/Servicio'}),
        }


class JustificacionForm2(ModelForm):

    class Meta:
        model = Justificacion
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Informe 2019 para el 2020'}),
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad/Servicio'}),
        }

