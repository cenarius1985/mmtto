from django.urls import path
from .views import LicitacionDelete, LicitacionCreate, LicitacionDetailView,LicitacionUpdate, LicitacionListView, FiltroLicitacionListView

licitacion_patterns = ([
    path('licitacion/', LicitacionListView.as_view(), name='licitacion'),
    path('licitacion/<int:pk>/', LicitacionDetailView.as_view(), name='detaillicitacion'),
    path('create/licitacion', LicitacionCreate.as_view(), name='createlicitacion'),
    path('licitacion/update/<int:pk>/', LicitacionUpdate.as_view(), name='updatelicitacion'),
    path('licitacion/delete/<int:pk>/', LicitacionDelete.as_view(), name='deletelicitacion'),
    path('licitacion/filter/', FiltroLicitacionListView.as_view(), name='filtrolicitacion'),
], 'licitacion')