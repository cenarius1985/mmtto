from django.urls import path
from .views import InventarioListView, InventarioDetailView, InventarioCreate, FiltroInventarioListView, InventarioUpdate, InventarioDelete

urlpatterns = [
    path('inventario/', InventarioListView.as_view(), name='inventario'),
    path('create_inventario/', InventarioCreate.as_view(), name='create_inventario'),
    path('<int:pk>/', InventarioDetailView.as_view(), name='equipo'),
    path('filtro_inventario', FiltroInventarioListView.as_view(), name='filtroinventario'),
    path('inventario/update/<int:pk>/', InventarioUpdate.as_view(), name='inventarioupdate'),
    path('delete/inventario/<int:pk>/', InventarioDelete.as_view(), name='deleteinventario'),
    
]