from django.forms import ModelForm
from django import forms
from .models import kilosservicio


class KilosservicioForm(ModelForm):
    
    class Meta:
        model = kilosservicio
        fields = "__all__"
        widgets = {
        'Fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'serviciosolicita':forms.Select(attrs={'class':'form-control'}),
        'Cantidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}),

        }


class KilosservicioForm2(ModelForm):

    class Meta:
        model = kilosservicio
        fields = "__all__"
        widgets = {
        'Fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'serviciosolicita':forms.Select(attrs={'class':'form-control'}),
        'Cantidad': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Descripcion'}),
        }

