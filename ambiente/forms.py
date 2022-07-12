from django.forms import ModelForm
from django import forms
from .models import ambiente


class AmbienteForm(ModelForm):
    class Meta:
        model = ambiente
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fecharecepcion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Informe'}),
        'desde': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad de Origen'}),
        'hacia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad de Destino'}),
        'recepcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Recepcionado Por'}),
        'documento' :forms.Select(attrs={'class':'form-control'}),
        }


class AmbienteForm2(ModelForm):

    class Meta:
        model = ambiente
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fecharecepcion': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Informe 2019 para el 2020'}),
        'recepcion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Recepcionado Por:'}),
        'desde': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad de Origen'}),
        'hacia': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Unidad de Destino'}),
        'documento' :forms.Select(attrs={'class':'form-control'}),
        }

