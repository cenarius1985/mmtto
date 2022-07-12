from django.forms import ModelForm
from django import forms
from .models import Guia


class GuiaForm(ModelForm):
    class Meta:
        model = Guia
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fecharecepcion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Informe'}),
        'numero': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Guia y Factura'}),
        'monto': forms.TextInput(attrs={'class':'form-control', 'placeholder':'valor'}),
        'documento' :forms.Select(attrs={'class':'form-control'}),
        }

class GuiaForm2(ModelForm):

    class Meta:
        model = Guia
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fecharecepcion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Informe 2019 para el 2020'}),
        'numero': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Guia y Factura'}),
        'monto': forms.TextInput(attrs={'class':'form-control', 'placeholder':'valor'}),
        'documento' :forms.Select(attrs={'class':'form-control'}),
        }

