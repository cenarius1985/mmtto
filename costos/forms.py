from django.forms import ModelForm
from django import forms
from .models import costos


class CostosForm(ModelForm):

    class Meta:
        model = costos
        fields = "__all__"
        widgets = {

        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fechae': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'proveedor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Proveedor'}),
        'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
        'criticorelevante': forms.Select(attrs={'class':'form-control'}),
        'serviciosolicita': forms.Select(attrs={'class':'form-control'}),
        'numerofactura': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Factura'}),
        'convenio': forms.Select(attrs={'class':'form-control'}),
        'numerolicitacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'898-01-LP19'}),
        'numeroordencompra': forms.TextInput(attrs={'class':'form-control', 'placeholder':'898-01-LP19'}),
        'monto': forms.TextInput(attrs={'class':'form-control', 'placeholder':'sin puntos ni comas'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control'}),
        'mantenimiento': forms.Select(attrs={'class':'form-control'}),
        
        }


class CostosForm2(ModelForm):

    class Meta:
        model = costos
        fields = "__all__"
        widgets = {
        
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechae': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'proveedor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Proveedor'}),
        'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
        'criticorelevante': forms.Select(attrs={'class':'form-control'}),
        'serviciosolicita': forms.Select(attrs={'class':'form-control'}),
        'numerofactura': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Factura'}),
        'convenio': forms.Select(attrs={'class':'form-control'}),
        'numerolicitacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'898-01-LP19'}),
        'numeroordencompra': forms.TextInput(attrs={'class':'form-control', 'placeholder':'898-01-LP19'}),
        'monto': forms.TextInput(attrs={'class':'form-control', 'placeholder':'sin puntos ni comas'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control'}),
        'mantenimiento': forms.Select(attrs={'class':'form-control'}),
        }

