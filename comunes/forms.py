from django.forms import ModelForm
from django import forms
from .models import comunes


class ComunesForm(ModelForm):

    class Meta:
        model = comunes
        fields = "__all__"
        widgets = {
        
        'numerofactura': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Factura'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'primerperiodo': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'segundoperiodo': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fechaemision': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'watts': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar Consumo Watts o Metros Cubicos Agua'}),
        'total': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar total de la Factura'}),
        'sector': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Casa Azul/Casa Verde etc.'}),
        'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar Direccion'}),
        'numeromedidor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero del Medidor'}),
        'numerocliente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Cliente'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control'}),
        'agualuz': forms.Select(attrs={'class':'form-control'}),
        }


class ComunesForm2(ModelForm):

    class Meta:
        model = comunes
        fields = "__all__"
        widgets = {
        
        'numerofactura': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Factura'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'primerperiodo': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'segundoperiodo': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechaemision': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'watts': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar Consumo Watts o Metros Cubicos Agua'}),
        'total': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar total de la Factura'}),
        'sector': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Casa Azul/Casa Verde etc.'}),
        'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Indicar Direccion'}),
        'numeromedidor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero del Medidor'}),
        'numerocliente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Cliente'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control'}),
        'agualuz': forms.Select(attrs={'class':'form-control'}),
        }

