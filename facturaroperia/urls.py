from django.urls import path
from .views import FacturaroperiaDelete, FacturaroperiaCreate, FacturaroperiaDetailView,FacturaroperiaUpdate, FacturaroperiaListView, FiltroFacturaroperiaListView

facturaroperia_patterns = ([
    path('facturaroperia/', FacturaroperiaListView.as_view(), name='facturaroperia'),
    path('facturaroperia/<int:pk>/', FacturaroperiaDetailView.as_view(), name='detailfacturaroperia'),
    path('create/facturaroperia', FacturaroperiaCreate.as_view(), name='createfacturaroperia'),
    path('facturaroperia/update/<int:pk>/', FacturaroperiaUpdate.as_view(), name='updatefacturaroperia'),
    path('facturaroperia/delete/<int:pk>/', FacturaroperiaDelete.as_view(), name='deletefacturaroperia'),
    path('facturaroperia/filter/', FiltroFacturaroperiaListView.as_view(), name='filtrofacturaroperia'),
], 'facturaroperia')