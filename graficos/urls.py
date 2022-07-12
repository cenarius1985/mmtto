from django.urls import path
from .views import GraficosRoperiaView

urlpatterns = [
    path('tablero/roperia', GraficosRoperiaView.as_view(), name='graficoroperia'),
   
    
]