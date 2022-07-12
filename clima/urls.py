from django.urls import path
from .views import ClimaDelete, ClimaCreate, ClimaDetailView,ClimaUpdate, ClimaListView, FiltroClimaListView

clima_patterns = ([
    path('clima/', ClimaListView.as_view(), name='clima'),
    path('clima/<int:pk>/', ClimaDetailView.as_view(), name='detailclima'),
    path('create/clima', ClimaCreate.as_view(), name='createclima'),
    path('clima/update/<int:pk>/', ClimaUpdate.as_view(), name='updateclima'),
    path('clima/delete/<int:pk>/', ClimaDelete.as_view(), name='deleteclima'),
    path('clima/filter/', FiltroClimaListView.as_view(), name='filtroclima'),
], 'clima')