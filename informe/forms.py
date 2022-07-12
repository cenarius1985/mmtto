from django.forms import ModelForm
from django import forms
from .models import Informes


class InformesForm(ModelForm):
    class Meta:
        model = Informes
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Informe 2019 para el 2020'}),
        }


class InformesForm2(ModelForm):

    class Meta:
        model = Informes
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Informe 2019 para el 2020'}),
        }

