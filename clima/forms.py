from django.forms import ModelForm
from django import forms
from .models import clima


class ClimaForm(ModelForm):

    class Meta:
        model = clima
        fields = "__all__"
        widgets = {

        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Servicio'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Serie'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'responsable': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Empresa de Mantenimiento'}),
        'frecuencia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Frecuencia'}),
        'fecha_baja': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),   
        'estado' :forms.Select(attrs={'class':'form-control'}),     


        }


class ClimaForm2(ModelForm):

    class Meta:
        model = clima
        fields = "__all__"
        widgets = {
        
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Servicio'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Serie'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'responsable': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Empresa de Mantenimiento'}),
        'frecuencia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Frecuencia'}),
        'fecha_baja': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'estado' :forms.Select(attrs={'class':'form-control'}),
        }

