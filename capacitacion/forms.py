from django.forms import ModelForm
from django import forms
from .models import Capacitacion


class CapacitacionForm(ModelForm):
    class Meta:
        model = Capacitacion
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Capacitacion'}),
        'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Clase'}),
        'modulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Modulo'}),
        }


class CapacitacionForm2(ModelForm):

    class Meta:
        model = Capacitacion
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Capacitacion'}),
        'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre Clase'}),
        'modulo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Modulo'}),
        }

