from django.forms import ModelForm
from django import forms
from .models import Bases


class BasesForm(ModelForm):
    class Meta:
        model = Bases
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Informe de Bases'}),
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad/Servicio'}),
        }


class BasesForm2(ModelForm):

    class Meta:
        model = Bases
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Informe 2019 para el 2020'}),
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad/Servicio'}),
        }

