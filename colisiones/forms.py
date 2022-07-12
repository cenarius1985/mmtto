from django.forms import ModelForm
from django import forms
from .models import colisiones


class ColisionesForm(ModelForm):
    class Meta:
        model = colisiones
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'colision': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hora de Colision'}),
        'fechasda': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'unidad':forms.Select(attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Conductor'}),
        'patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Patente con numero verificador'}),
        'valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'200.000'}),
        'salida': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hora de Salida'}),
        'inicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'HCV'}),
        'final': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valparaíso'}),
        'kilometraje': forms.TextInput(attrs={'class':'form-control', 'placeholder':'100.000'}),
        'numeromotor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'100.000'}),
        'numerochasis': forms.TextInput(attrs={'class':'form-control', 'placeholder':'100.000'}),
        }


class ColisionesForm2(ModelForm):

    class Meta:
        model = colisiones
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'colision': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hora de Colision'}),
        'fechasda': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'unidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SSGG/SAMU/URGENCIA'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Conductor'}),
        'patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Patente con numero verificador'}),
        'valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'200.000'}),
        'salida': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Horario de Salida'}),
        'inicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'HCV'}),
        'final': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valparaíso'}),
        'kilometraje': forms.TextInput(attrs={'class':'form-control', 'placeholder':'100.000'}),
        'numeromotor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'100.000'}),
        'numerochasis': forms.TextInput(attrs={'class':'form-control', 'placeholder':'100.000'}),
        }

