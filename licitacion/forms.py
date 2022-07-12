from django.forms import ModelForm
from django import forms
from .models import licitacion


class LicitacionForm(ModelForm):

    class Meta:
        model = licitacion
        fields = "__all__"
        widgets = {
        
        'Nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de Licitacion'}),
        'detalle':  forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalle'}),
        'ID_Mercado_Publico': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID Mercado Publico'}),
        'Monto': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Monto Asignado'}),
        'Fecha_Publicacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'Fecha_Adjudicacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'estadolicitacion': forms.Select(attrs={'class':'form-control'}),
        'adjudicado': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Adjudicado'}),
        'fechatermino': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'observaciones': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
        
        }

class LicitacionForm2(ModelForm):
    
    class Meta:
        model = licitacion
        fields = "__all__"
        widgets = {
        
        'Nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre de Licitacion'}),
        'detalle': forms.Textarea(attrs={'class':'form-control'}),
        'ID_Mercado_Publico': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ID de Mercado Publico'}),
        'Monto': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Monto Asignado'}),
        'Fecha_Publicacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'Fecha_Adjudicacion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'estadolicitacion': forms.Select(attrs={'class':'form-control'}),
        'adjudicado': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Adjudicado'}),
        'fechatermino': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control',}),
        'observaciones': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Observaciones'}),

        }
