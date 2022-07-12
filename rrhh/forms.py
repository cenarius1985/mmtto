from django.forms import ModelForm
from django import forms
from .models import rrhh


class RRHHForm(ModelForm):

    class Meta:
        model = rrhh
        fields = "__all__"
        widgets = {
        'nombres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fernando Jose'}),
        'apellidos': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'cargo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'estado': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'unidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'funcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'contrato': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        }


class RRHHForm2(ModelForm):

    class Meta:
        model = rrhh
        fields = "__all__"
        widgets = {
        'nombres': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fernando Jose'}),
        'apellidos': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'cargo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'estado': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'unidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'funcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        'contrato': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ramirez Sarmiento'}),
        }

