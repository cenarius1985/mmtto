from django.forms import ModelForm
from django import forms
from .models import infraestructura


class InfraestructuraForm(ModelForm):

    class Meta:
        model = infraestructura
        fields = "__all__"
        widgets = {

        'sistema': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Calefaccion Centralizada'}),
        'ubicacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primer Piso'}),
        'frecuencia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Mantenciones Anuales'}),
        'responsable': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Mantenciones Anuales'}),

        }


class InfraestructuraForm2(ModelForm):

    class Meta:
        model = infraestructura
        fields = "__all__"
        widgets = {
        
        'sistema': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Calefaccion Centralizada'}),
        'ubicacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Primer Piso'}),
        'frecuencia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Mantenciones Anuales'}),
        'responsable': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Mantenciones Anuales'}),

        }

