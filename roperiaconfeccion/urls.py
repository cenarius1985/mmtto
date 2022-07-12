from django.urls import path
from .views import RoperiaconfeccionDelete, RoperiaconfeccionCreate, RoperiaconfeccionDetailView,RoperiaconfeccionUpdate, RoperiaconfeccionListView, FiltroRoperiaconfeccionListView

roperiaconfeccion_patterns = ([
    path('roperiaconfeccion/', RoperiaconfeccionListView.as_view(), name='roperiaconfeccion'),
    path('roperiaconfeccion/<int:pk>/', RoperiaconfeccionDetailView.as_view(), name='detailroperiaconfeccion'),
    path('create/roperiaconfeccion', RoperiaconfeccionCreate.as_view(), name='createroperiaconfeccion'),
    path('roperiaconfeccion/update/<int:pk>/', RoperiaconfeccionUpdate.as_view(), name='updateroperiaconfeccion'),
    path('roperiaconfeccion/delete/<int:pk>/', RoperiaconfeccionDelete.as_view(), name='deleteroperiaconfeccion'),
    path('roperiaconfeccion/filter/', FiltroRoperiaconfeccionListView.as_view(), name='filtroroperiaconfeccion'),
], 'roperiaconfeccion')