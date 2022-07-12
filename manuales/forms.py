from django.forms import ModelForm
from django import forms
from .models import Manuales


class ManualesForm(ModelForm):
    class Meta:
        model = Manuales
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca del Equipo'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo del Equipo'}),
        'representante': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Representante de la Marca'}),
        }


class ManualesForm2(ModelForm):

    class Meta:
        model = Manuales
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca del Equipo'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo del Equipo'}),
        'representante': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Representante de la Marca'}),
        }

