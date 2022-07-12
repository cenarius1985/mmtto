from django.urls import path
from .views import GuiaDelete, GuiaCreate, GuiaDetailView,GuiaUpdate, GuiaListView, FiltroGuiaListView

guia_patterns = ([
    path('guia/', GuiaListView.as_view(), name='guia'),
    path('guia/<int:pk>/', GuiaDetailView.as_view(), name='detailguia'),
    path('create/guia', GuiaCreate.as_view(), name='createguia'),
    path('guia/update/<int:pk>/', GuiaUpdate.as_view(), name='updateguia'),
    path('guia/delete/<int:pk>/', GuiaDelete.as_view(), name='deleteguia'),
    path('guia/filter/', FiltroGuiaListView.as_view(), name='filtroguia'),
], 'guia')