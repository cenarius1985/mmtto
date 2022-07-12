from django.urls import path
from .views import OrdenestalleresDelete, OrdenestalleresCreate, OrdenestalleresDetailView,OrdenestalleresUpdate, OrdenestalleresListView, FiltroOrdenestalleresListView

ordenestalleres_patterns = ([
    path('ordenestalleres/', OrdenestalleresListView.as_view(), name='ordenestalleres'),
    path('ordenestalleres/<int:pk>/', OrdenestalleresDetailView.as_view(), name='detailordenestalleres'),
    path('create/ordenestalleres', OrdenestalleresCreate.as_view(), name='createordenestalleres'),
    path('ordenestalleres/update/<int:pk>/', OrdenestalleresUpdate.as_view(), name='updateordenestalleres'),
    path('ordenestalleres/delete/<int:pk>/', OrdenestalleresDelete.as_view(), name='deleteordenestalleres'),
    path('ordenestalleres/filter/', FiltroOrdenestalleresListView.as_view(), name='filtroordenestalleres'),
], 'ordenestalleres')