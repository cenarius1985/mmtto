from django.urls import path
from .views import ManualesDelete, ManualesCreate, ManualesDetailView,ManualesUpdate, ManualesListView, FiltroManualesListView

manuales_patterns = ([
    path('manuales/', ManualesListView.as_view(), name='manuales'),
    path('manuales/<int:pk>/', ManualesDetailView.as_view(), name='detailmanuales'),
    path('create/manuales', ManualesCreate.as_view(), name='createmanuales'),
    path('manuales/update/<int:pk>/', ManualesUpdate.as_view(), name='updatemanuales'),
    path('manuales/delete/<int:pk>/', ManualesDelete.as_view(), name='deletemanuales'),
    path('manuales/filter/', FiltroManualesListView.as_view(), name='filtromanuales'),
], 'manuales')