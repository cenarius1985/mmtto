from django import forms
from .models import ParqueAutomotriz
from django.forms import ModelForm

class AmbulanciaForm(ModelForm):

    class Meta:
        model = ParqueAutomotriz
        fields = "__all__"
        widgets = {
        'Movil': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo de Movil'}),
        'km_anterior' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Km Anterior'}),
        'km_real' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometro Realizado'}),
        'proximo_cambio' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Proximo Mantenimiento'}),
        'km_programado' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mantenimiento Programado'}),
        'Patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Patente'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Modelo'}),
        'Servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Servicio o Centro de Costos'}),
        'inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Inventario'}),
        'tecnico1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Tecnico'}),
        'tecnico2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Tecnico'}),
        'responsable': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Jefe de MMTTO'}),
        'observacion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}), 
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),  
        }

class AmbulanciaForm2(ModelForm):

    class Meta:
        model = ParqueAutomotriz
        fields = "__all__"
        widgets = {
        'Movil': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo de Movil'}),
        'km_anterior' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Km Anterior'}),
        'km_real' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometro Realizado'}),
        'proximo_cambio' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Proximo Mantenimiento'}),
        'km_programado' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Mantenimiento Programado'}),
        'Patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Patente'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':' Modelo'}),
        'Servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Servicio o Centro de Costos'}),
        'inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Inventario'}),
        'tecnico1': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Tecnico'}),
        'tecnico2': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Tecnico'}),
        'responsable': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Jefe de MMTTO'}),
        'observacion': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}), 
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),  
        }