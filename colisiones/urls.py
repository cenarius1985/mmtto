from django.urls import path
from .views import ColisionesDelete, ColisionesCreate, ColisionesDetailView,ColisionesUpdate, ColisionesListView, FiltroColisionesListView

colisiones_patterns = ([
    path('colisiones/', ColisionesListView.as_view(), name='colisiones'),
    path('colisiones/<int:pk>/', ColisionesDetailView.as_view(), name='detailcolisiones'),
    path('create/colisiones', ColisionesCreate.as_view(), name='createcolisiones'),
    path('colisiones/update/<int:pk>/', ColisionesUpdate.as_view(), name='updatecolisiones'),
    path('colisiones/delete/<int:pk>/', ColisionesDelete.as_view(), name='deletecolisiones'),
    path('colisiones/filter/', FiltroColisionesListView.as_view(), name='filtrocolisiones'),
], 'colisiones')