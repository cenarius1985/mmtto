from django.forms import ModelForm
from django import forms
from .models import facturaroperia


class FacturaroperiaForm(ModelForm):

    class Meta:
        model = facturaroperia
        fields = "__all__"
        widgets = {
        
        'numerofactura': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Factura'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'proveedor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar Nombre del proovedor'}),
        'monto': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor total de la Factura'}),
        'numeroordencompra': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Orden de Compra'}),
        'estadofactura': forms.Select(attrs={'class':'form-control'}),
        'fechaemision': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fechatramitacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'servicio': forms.Select(attrs={'class':'form-control'}),
        'detalle': forms.Textarea(attrs={'class':'form-control'}),
        }
        
class FacturaroperiaForm2(ModelForm):
    
    class Meta:
        model = facturaroperia
        fields = "__all__"
        widgets = {
        
        'numerofactura': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Factura'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'proveedor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar Nombre del proovedor'}),
        'monto': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor total de la Factura'}),
        'numeroordencompra': forms.TextInput(attrs={'class':'form-control'}),
        'estadofactura': forms.Select(attrs={'class':'form-control'}),
        'fechaemision': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechatramitacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'servicio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Servicio Prestado'}),
        'detalle': forms.Textarea(attrs={'class':'form-control'}),

        }
