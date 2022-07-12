from django.forms import ModelForm
from django import forms
from .models import hhee


class HHEEForm(ModelForm):

    class Meta:
        model = hhee
        fields = "__all__"
        widgets = {

        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Funcionario'}),
        'hhee': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de horas'}),
        'motivo': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Motivo de HHEE'}),
        }

class HHEEForm2(ModelForm):

    class Meta:
        model = hhee
        fields = "__all__"
        widgets = {
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Funcionario'}),
        'hhee': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de horas'}),
        'motivo': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Motivo de HHEE'}),
        }

