from django.forms import ModelForm
from django import forms
from .models import MantenimientoExterno

class ExternoForm(ModelForm):

    class Meta:
        model = MantenimientoExterno
        fields = "__all__"
        widgets = {
        'Modelo_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'Inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N°Inventario'}),
        'Serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Serie'}),
        'Numero': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Orden de Trabajo'}),
        'Marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'Tecnico': forms.TextInput(attrs={'class':'form-control', 'placeholder':'"Nombre del Tecnico"'}),
        'Empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Empresa'}),
        'Nombre_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
        'Unidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Servicio'}),
        'Observaciones': forms.Textarea(attrs={'class':'form-control', 'placeholder':''}),
        'Detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalles'}), 
        'Fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'Fecha_Equipo_Operativo': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'Fecha_Equipo_Baja': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'Tipo_Mantenimiento': forms.Select(attrs={'class':'form-control'}),
        'Critico_Relevante': forms.Select(attrs={'class':'form-control'}),
        'Horas': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Horas Fuera de Servicio'}),
        }
    
class ExternoForm2(ModelForm):
    class Meta:
            model = MantenimientoExterno
            fields = "__all__"
            widgets = {
            'Modelo_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
            'Inventario': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N°Inventario'}),
            'Serie': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Serie'}),
            'Numero': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Serie'}),
            'Marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
            'Tecnico': forms.TextInput(attrs={'class':'form-control', 'placeholder':'"Nombre del Tecnico"'}),
            'Empresa': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de la Empresa'}),
            'Nombre_Equipo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Equipo'}),
            'Unidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Servicio'}),
            'Observaciones': forms.Textarea(attrs={'class':'form-control', 'placeholder':''}),
            'Detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalles'}), 
            'Fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
            'Fecha_Equipo_Operativo': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
            'Fecha_Equipo_Baja': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
            'Tipo_Mantenimiento': forms.Select(attrs={'class':'form-control'}),
            'Critico_Relevante': forms.Select(attrs={'class':'form-control'}),
            'Horas': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Horas Fuera de Servicio'}),
            }