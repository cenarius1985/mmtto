from django.forms import ModelForm
from django import forms
from .models import ropaexterno


class RopaexternoForm(ModelForm):
    
    class Meta:
        model = ropaexterno
        fields = "__all__"
        widgets = {
        'Nombre_Empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de Empresa'}),
        'Guia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero Guia'}),
        'Fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'Detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
        'Cantidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilos'}),
        'Precio_Unitario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Precio Unitario'}),
        'Valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor'}),
        }


class RopaexternoForm2(ModelForm):

    class Meta:
        model = ropaexterno
        fields = "__all__"
        widgets = {
        'Nombre_Empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de Empresa'}),
        'Guia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero Guia'}),
        'Fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'Detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
        'Cantidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilos'}),
        'Precio_Unitario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Precio Unitario'}),
        'Valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor'}),
        }

