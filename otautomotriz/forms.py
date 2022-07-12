from django.forms import ModelForm
from django import forms
from .models import otautomotriz


class OtautomotrizForm(ModelForm):

    class Meta:
        model = otautomotriz
        fields = "__all__"
        widgets = {
        
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'numeroorden': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de OT'}),
        'patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Patente'}),
        'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalle'}),
        'fechaingreso': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'kilometraje': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Factura'}),
        'fechaegreso': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'unidad': forms.Select(attrs={'class':'form-control'}),
        'total': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar total de la Factura'}),
        'tipo_mantenimiento': forms.Select(attrs={'class':'form-control'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control'}),
       
        }


class OtautomotrizForm2(ModelForm):

    class Meta:
        model = otautomotriz
        fields = "__all__"
        widgets = {
        
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'numeroorden': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Factura'}),
        'patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Factura'}),
        'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Factura'}),
        'fechaingreso': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'kilometraje': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Factura'}),
        'fechaegreso': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'unidad': forms.Select(attrs={'class':'form-control'}),
        'total': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar total de la Factura'}),
        'tipo_mantenimiento': forms.Select(attrs={'class':'form-control'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control'}),
       
     }

    