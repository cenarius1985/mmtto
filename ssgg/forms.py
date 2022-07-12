from django.forms import ModelForm
from django import forms
from .models import cartola, moviles

class CartolaForm(ModelForm):

    class Meta:
        model = cartola
        fields = ['patente','fecha','kmi','kmf','combustible','litros','valor','uo','pauta1']
        widgets = {
        
        'patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Patente'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}), 
        'kmi': forms.TextInput(attrs={'class':'form-control', 'placeholder':'kilometraje Inicial'}),
        'kmf': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometraje Final'}),
        'kmdt': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometraje Diario Recorrido'}),
        'combustible': forms.Select(attrs={'class':'form-control'}),
        'litros': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Litros'}),
        'valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor de la Recarga de Combustible'}),
        'uo': forms.Select(attrs={'class':'form-control'}),
        'pauta1': forms.Select(attrs={'class':'form-control'}),
        }

class CartolaForm2(ModelForm):
    class Meta:
        model = cartola
        fields = "__all__"
        widgets = {
        
        'patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Patente'}),
        'fecha': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'kmi': forms.TextInput(attrs={'class':'form-control', 'placeholder':'kilometraje Inicial'}),
        'kmf': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometraje Final'}),
        'kmdt': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometraje Diario Recorrido'}),
        'combustible': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo de Combustible'}),
        'litros': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Litros'}),
        'valor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Valor de la Recarga de Combustible'}),
        'uo': forms.Select(attrs={'class':'form-control'}),
        'pauta1': forms.Select(attrs={'class':'form-control'}),
        'fechar': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechai': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),

        }



class MovilForm(ModelForm):

    class Meta:
        model = moviles
        fields = "__all__"
        widgets = {
        
        'patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Patente'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'numeromotor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Motor'}),
        'numerochasis': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Chasis'}),
        'tipo': forms.Select(attrs={'class':'form-control'}),
        'fechar': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'fechai': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}), 
        'combustible': forms.Select(attrs={'class':'form-control'}),
        'kilometraje': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometraje de Mantenimiento'}), 
        'servicio': forms.Select(attrs={'class':'form-control'}),
        'baja': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        'estado': forms.Select(attrs={'class':'form-control'}),
        
        }

    
   
    

class MovilForm2(ModelForm):
    class Meta:
        model = moviles
        fields = "__all__"
        widgets = {
        'patente': forms.TextInput(attrs={'class':'form-control', 'placeholder':'N° Patente'}),
        'marca': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Marca'}),
        'modelo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Modelo'}),
        'numeromotor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Motor'}),
        'numerochasis': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Numero de Chasis'}),
        'tipo': forms.Select(attrs={'class':'form-control'}),
        'fechar': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'fechai': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}), 
        'combustible': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tipo de Combustible'}),
        'kilometraje': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Kilometraje de Mantenimiento'}), 
        'servicio': forms.Select(attrs={'class':'form-control'}),
        'baja': forms.DateInput(format=('%d/%m/%Y'), attrs={'class':'form-control'}),
        'estado': forms.Select(attrs={'class':'form-control'}),
        }