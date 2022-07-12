from django.forms import ModelForm
from django import forms
from .models import industriales


class IndustrialesForm(ModelForm):

    class Meta:
        model = industriales
        fields = "__all__"
        widgets = {

        'Servicio_Clinico': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ubicacion'}),
        'Clase': forms.Select(attrs={'class':'form-control'}),
        'Subclase': forms.Select(attrs={'class':'form-control'}),
        'Nombre_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
        'Marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca del Equipo'}),
        'Modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo del Equipo'}),
        'Serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Serie del Equipo'}),
        'Numero_Inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Inventario'}),
        'Valor_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor del Equipo'}),
        'Instalacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'Vida_Util': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vida Util del Equipo'}),
        'Condicion': forms.Select(attrs={'class':'form-control'}),
        'Estado':forms.Select(attrs={'class':'form-control'}), 
        'criticoapoyo':forms.Select(attrs={'class':'form-control'}),
        'Frecuencia' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Frecuencia'}),
        'Responsable': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Empresa Encargada de Mantenimiento'}),
        'RUT': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Empresa Encargada de Mantenimiento'}),
        'fechaIG': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fechaTG': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fechaBaja': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }


class IndustrialesForm2(ModelForm):

    class Meta:
        model = industriales
        fields = "__all__"
        widgets = {
        
        'Servicio_Clinico': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ubicacion'}),
        'Clase': forms.Select(attrs={'class':'form-control'}),
        'Subclase': forms.Select(attrs={'class':'form-control'}),
        'Nombre_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
        'Marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca del Equipo'}),
        'Modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo del Equipo'}),
        'Serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Serie del Equipo'}),
        'Numero_Inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Inventario'}),
        'Valor_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor del Equipo'}),
        'Instalacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'Vida_Util': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Vida Util del Equipo'}),
        'Condicion': forms.Select(attrs={'class':'form-control'}),
        'Estado':forms.Select(attrs={'class':'form-control'}), 
        'criticoapoyo':forms.Select(attrs={'class':'form-control'}),
        'Frecuencia' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Frecuencia'}),
        'Responsable': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Empresa Encargada de Mantenimiento'}),
        'RUT': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Empresa Encargada de Mantenimiento'}),
        'fechaIG': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechaTG': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechaBaja': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        }

