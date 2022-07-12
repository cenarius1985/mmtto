from django.urls import path
from .views import CostosDelete, CostosCreate, CostosDetailView,CostosUpdate, CostosListView, FiltroCostosListView

costos_patterns = ([
    path('costos/', CostosListView.as_view(), name='costos'),
    path('costos/<int:pk>/', CostosDetailView.as_view(), name='detailcostos'),
    path('create/costos', CostosCreate.as_view(), name='createcostos'),
    path('costos/update/<int:pk>/', CostosUpdate.as_view(), name='updatecostos'),
    path('costos/delete/<int:pk>/', CostosDelete.as_view(), name='deletecostos'),
    path('costos/filter/', FiltroCostosListView.as_view(), name='filtrocostos'),
], 'costos')