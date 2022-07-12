from django.forms import ModelForm
from django import forms
from .models import actas


class ActasForm(ModelForm):
    
    class Meta:
        model = actas
        fields = "__all__"
        widgets = {

        'Fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'serviciosolicita':forms.Select(attrs={'class':'form-control'}),
        'Proveedor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Empresa'}),
        'Guia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Guia Despacho'}),
        'OC': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Orden de Compra'}),
        'Licitacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Licitacion'}),
        'Detalle': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
        }


class ActasForm2(ModelForm):

    class Meta:
        model = actas
        fields = "__all__"
        widgets = {
        'Fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'serviciosolicita':forms.Select(attrs={'class':'form-control'}),
        'Proveedor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Empresa'}),
        'Guia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Guia Despacho'}),
        'OC': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Guia Despacho'}),
        'Licitacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Licitacion'}),
        'Detalle': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
        }

