from django.forms import ModelForm
from django import forms
from .models import proyectos


class ProyectosForm(ModelForm):

    class Meta:
        model = proyectos
        fields = "__all__"
        widgets = {

        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Proyecto'}),
        'fechaa': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fechai': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fechat': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        'duracion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duracion del Proyecto en Semanas'}),

        }


class ProyectosForm2(ModelForm):

    class Meta:
        model = proyectos
        fields = "__all__"
        widgets = {
        
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre del Proyecto'}),
        'fechaa': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechai': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechat': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'descripcion': forms.Textarea(attrs={'class':'form-control'}),
        'duracion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Duracion del Proyecto en Semanas'}),
        }

