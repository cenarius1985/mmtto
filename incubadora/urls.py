from django.urls import path
from .views import IncubadoraCreate, IncubadoraDetailView

incubadora_patterns = ([
    path('create_incubadora/', IncubadoraCreate.as_view(), name='create_incubadora'),
    path('<int:pk>/<slug:slug>/', IncubadoraDetailView.as_view(), name='incubadora'),
], 'incubadoras')