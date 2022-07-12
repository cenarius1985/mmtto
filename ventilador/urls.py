from django.urls import path
from .views import VentiladorCreate, VentiladorDetailView

ventilador_patterns = ([
    path('create_ventilador/', VentiladorCreate.as_view(), name='create_ventilador'),
    path('<int:pk>/<slug:slug>/',VentiladorDetailView.as_view(), name='ventilador'),
], 'ventiladores')