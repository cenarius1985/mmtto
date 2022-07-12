from django.urls import path
from .views import ExternoCreate, ExternoDetailView, ExternoListView, FiltroExternoListView, ExternoUpdate, ExternoDelete

urlpatterns = [
    path('externolista/', ExternoListView.as_view(), name='externolistview'),
    path('create_externo/', ExternoCreate.as_view(), name='createexterno'),
    path('externo/<int:pk>/', ExternoDetailView.as_view(), name='matenimientoexterno'),
    path('filtro_externo', FiltroExternoListView.as_view(), name='filtroexterno'),
    path('externo/update/<int:pk>/', ExternoUpdate.as_view(), name='externoupdate'),
    path('externo/delete/<int:pk>/', ExternoDelete.as_view(), name='deleteexterno'),
    ]