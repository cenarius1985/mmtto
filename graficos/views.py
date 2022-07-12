from django.shortcuts import render
from django.views.generic.base import TemplateView

class GraficosRoperiaView(TemplateView):
    
    template_name = "graficos/graficosroperia.html"