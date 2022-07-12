from django.urls import path
from .views import RRHHDelete, RRHHCreate, RRHHDetailView,RRHHUpdate, RRHHListView, FiltroRRHHListView

rrhh_patterns = ([
    path('rrhh/', RRHHListView.as_view(), name='rrhh'),
    path('rrhh/<int:pk>/', RRHHDetailView.as_view(), name='detailrrhh'),
    path('create/rrhh', RRHHCreate.as_view(), name='createrrhh'),
    path('rrhh/update/<int:pk>/', RRHHUpdate.as_view(), name='updaterrhh'),
    path('rrhh/delete/<int:pk>/', RRHHDelete.as_view(), name='deleterrhh'),
    path('rrhh/filter/', FiltroRRHHListView.as_view(), name='filtrorrhh'),
], 'rrhh')