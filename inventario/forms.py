from django.forms import ModelForm
from django import forms
from .models import inventario



class InventarioForm(ModelForm):

    class Meta:
        model = inventario
        fields = "__all__"
        widgets = {
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Servicio Clinico o CC'}),
        'clase': forms.Select(attrs={'class':'form-control'}),
        'subclase': forms.Select(attrs={'class':'form-control'}),
        'nombre_equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre del Equipo'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'ano': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Año de Instalacion'}),
        'serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Serie'}),
        'licitacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar N° de Licitacion'}),
        'valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor del Equipo'}),
        'inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Inventario'}),
        'empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Empresa'}),
        'rut': forms.TextInput(attrs={'class':'form-control', 'placeholder':'12345678-9'}),
        'garantia_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'garantia_final': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'garantia_final': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fecha':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'vida_util': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vida Util'}),
        'contrato' :forms.Select(attrs={'class':'form-control'}),
        'estado' :forms.Select(attrs={'class':'form-control'}),
        'critico_apoyo' :forms.Select(attrs={'class':'form-control'}),
        'frecuencia' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Frecuencia de Mantenimiento'}),
        'fecha_baja':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class InventarioForm2(ModelForm):

    class Meta:
        model = inventario
        fields = "__all__"
        widgets = {
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Servicio Clinico o CC'}),
        'clase': forms.Select(attrs={'class':'form-control'}),
        'subclase': forms.Select(attrs={'class':'form-control'}),
        'nombre_equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar Nombre del Equipo'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Serie'}),
        'ano': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Año de Instalacion'}),
        'licitacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresar N° de Licitacion'}),
        'valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor del Equipo'}),
        'inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Inventario'}),
        'empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Empresa'}),
        'rut': forms.TextInput(attrs={'class':'form-control', 'placeholder':'12345678-9'}),
        'garantia_inicio': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'garantia_final': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'garantia_final': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fecha':forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'vida_util': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vida Util'}),
        'contrato' :forms.Select(attrs={'class':'form-control'}),
        'estado' :forms.Select(attrs={'class':'form-control'}),
        'critico_apoyo' :forms.Select(attrs={'class':'form-control'}),
        'frecuencia' :forms.TextInput(attrs={'class':'form-control', 'placeholder':'Frecuencia de Mantenimiento'}),
        'fecha_baja': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        }
