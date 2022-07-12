from django.urls import path
from .views import OrdenesDelete, OrdenesCreate, OrdenesDetailView,OrdenesUpdate, OrdenesListView, FiltroOrdenesListView

ordenes_patterns = ([
    path('ordenes/', OrdenesListView.as_view(), name='ordenes'),
    path('ordenes/<int:pk>/', OrdenesDetailView.as_view(), name='detailordenes'),
    path('create/ordenes', OrdenesCreate.as_view(), name='createordenes'),
    path('ordenes/update/<int:pk>/', OrdenesUpdate.as_view(), name='updateordenes'),
    path('ordenes/delete/<int:pk>/', OrdenesDelete.as_view(), name='deleteordenes'),
    path('ordenes/filter/', FiltroOrdenesListView.as_view(), name='filtroordenes'),
], 'ordenes')