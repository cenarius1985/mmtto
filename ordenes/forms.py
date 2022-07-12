from django.forms import ModelForm
from django import forms
from .models import ordenes


class OrdenesForm(ModelForm):

    class Meta:
        model = ordenes
        fields = "__all__"
        widgets = {

        'numerofolio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Folio'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalle de los Trabajos'}),
        'serviciosolicita' : forms.Select(attrs={'class':'form-control'}),
        'estadoOT': forms.Select(attrs={'class':'form-control'}),
        'valormano': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor Mano de Obra'}),
        'valormateriales': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor de Materiales'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones de los trabajos'}),
        }


class OrdenesForm2(ModelForm):

    class Meta:
        model = ordenes
        fields = "__all__"
        widgets = {
        'numerofolio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° de Folio'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'detalle': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Detalle de los Trabajos'}),
        'serviciosolicita' : forms.Select(attrs={'class':'form-control'}),
        'estadoOT': forms.Select(attrs={'class':'form-control'}),
        'valormano': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor Mano de Obra'}),
        'valormateriales': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor de Materiales'}),
        'observaciones': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Observaciones de los trabajos'}),
        }

