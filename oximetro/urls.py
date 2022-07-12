from django.urls import path
from .views import OximetroCreate, OximetroDetailView

oximetro_patterns = ([
    path('create_oximetro/', OximetroCreate.as_view(), name='create_oximetro'),
    path('<int:pk>/<slug:slug>/', OximetroDetailView.as_view(), name='oximetro'),
], 'oximetros')