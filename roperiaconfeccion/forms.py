from django.forms import ModelForm
from django import forms
from .models import roperiaconfeccion


class RoperiaconfeccionForm(ModelForm):
    
    class Meta:
        model = roperiaconfeccion
        fields = "__all__"
        widgets = {
        'Fecha_OC': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'Numero_Boleta': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero Boleta'}),
        'RUT': forms.TextInput(attrs={'class':'form-control', 'placeholder':'RUT'}),
        'Nombre_Empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de Empresa'}),
        'Detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion del Servicio'}),
        'Valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor'}),
        'OC': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Orden de Compra'}),
        }


class RoperiaconfeccionForm2(ModelForm):

    class Meta:
        model = roperiaconfeccion
        fields = "__all__"
        widgets = {
        'Fecha_OC': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'Numero_Boleta': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero Boleta'}),
        'RUT': forms.TextInput(attrs={'class':'form-control', 'placeholder':'RUT'}),
        'Nombre_Empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de Empresa'}),
        'Detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion del Servicio'}),
        'Valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor'}),
        'OC': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Orden de Compra'}),
        }

