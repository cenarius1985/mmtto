from django.urls import path
from .views import ProyectosDelete, ProyectosCreate, ProyectosDetailView,ProyectosUpdate, ProyectosListView, FiltroProyectosListView

proyectos_patterns = ([
    path('proyectos/', ProyectosListView.as_view(), name='proyectos'),
    path('proyectos/<int:pk>/', ProyectosDetailView.as_view(), name='detailproyectos'),
    path('create/proyectos', ProyectosCreate.as_view(), name='createproyectos'),
    path('proyectos/update/<int:pk>/', ProyectosUpdate.as_view(), name='updateproyectos'),
    path('proyectos/delete/<int:pk>/', ProyectosDelete.as_view(), name='deleteproyectos'),
    path('proyectos/filter/', FiltroProyectosListView.as_view(), name='filtroproyectos'),
], 'proyectos')