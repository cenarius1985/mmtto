from django.urls import path
from .views import FiltroEneroListView, FiltroInicioListView

gantt_patterns = ([
    path('gantt/', FiltroEneroListView.as_view(), name='enerogantt'),
    path('gantt/inicio', FiltroInicioListView.as_view(), name='iniciogantt'),
    
], 'gantt')