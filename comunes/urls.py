from django.urls import path
from .views import ComunesDelete, ComunesCreate, ComunesDetailView,ComunesUpdate, ComunesListView, FiltroComunesListView

comunes_patterns = ([
    path('comunes/', ComunesListView.as_view(), name='comunes'),
    path('comunes/<int:pk>/', ComunesDetailView.as_view(), name='detailcomunes'),
    path('create/comunes', ComunesCreate.as_view(), name='createcomunes'),
    path('comunes/update/<int:pk>/', ComunesUpdate.as_view(), name='updatecomunes'),
    path('comunes/delete/<int:pk>/', ComunesDelete.as_view(), name='deletecomunes'),
    path('comunes/filter/', FiltroComunesListView.as_view(), name='filtrocomunes'),
], 'comunes')