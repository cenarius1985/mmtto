from django.urls import path
from .views import MovilCreate, AmbulanciaDetailView, AmbulanciaListView, AmbulanciaUpdate, FiltroAmbulanciaListView, AmbulanciaDelete

ambulancia_patterns = ([
    path('createambulancia/', MovilCreate.as_view(), name='crearambulancia'),
    path('ambulancia_lista/', AmbulanciaListView.as_view(), name='listaambulancia'),
    path('<int:pk>/ambulancia',AmbulanciaDetailView.as_view(), name='ambulancia'),
    path('ambulancia/update/<int:pk>/', AmbulanciaUpdate.as_view(), name='ambulanciaupdate'),
    path('filtro_ambulancia', FiltroAmbulanciaListView.as_view(), name='filtroambulancia'),
     path('borrar/ambulancia/<int:pk>/', AmbulanciaDelete.as_view(), name='borrarambulancia'),

], 'ambulancias')