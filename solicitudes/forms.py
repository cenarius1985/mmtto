from django.forms import ModelForm
from django import forms
from .models import solicitudes


class SolicitudesForm(ModelForm):

    class Meta:
        model = solicitudes
        fields = "__all__"
        widgets = {

        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'numeroadquisicion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Registro Correlativo'}),
        'estadoOT': forms.Select(attrs={'class':'form-control'}),
        'servicioorigen' : forms.Select(attrs={'class':'form-control'}),
        'fechasda': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fechaabast': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalle de los Trabajos'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
        }

class SolicitudesForm2(ModelForm):

    class Meta:
        model = solicitudes
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'numeroadquisicion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalle de los Trabajos'}),
        'estadoOT': forms.Select(attrs={'class':'form-control'}),
        'servicioorigen' : forms.Select(attrs={'class':'form-control'}),
        'fechasda': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechaabast': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalle de los Trabajos'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
        }

