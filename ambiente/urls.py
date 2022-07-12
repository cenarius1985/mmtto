from django.urls import path
from .views import AmbienteDelete, AmbienteCreate, AmbienteDetailView,AmbienteUpdate, AmbienteListView, FiltroAmbienteListView

ambiente_patterns = ([
    path('ambiente/', AmbienteListView.as_view(), name='ambiente'),
    path('ambiente/<int:pk>/', AmbienteDetailView.as_view(), name='detailambiente'),
    path('create/ambiente', AmbienteCreate.as_view(), name='createambiente'),
    path('ambiente/update/<int:pk>/', AmbienteUpdate.as_view(), name='updateambiente'),
    path('ambiente/delete/<int:pk>/', AmbienteDelete.as_view(), name='deleteambiente'),
    path('ambiente/filter/', FiltroAmbienteListView.as_view(), name='filtroambiente'),
], 'ambiente')