from django.urls import path
from .views import HHEEDelete, HHEECreate, HHEEDetailView,HHEEUpdate, HHEEListView, FiltroHHEEListView

hhee_patterns = ([
    path('hhee/', HHEEListView.as_view(), name='hhee'),
    path('hhee/<int:pk>/', HHEEDetailView.as_view(), name='detailhhee'),
    path('create/hhee', HHEECreate.as_view(), name='createhhee'),
    path('hhee/update/<int:pk>/', HHEEUpdate.as_view(), name='updatehhee'),
    path('hhee/delete/<int:pk>/', HHEEDelete.as_view(), name='deletehhee'),
    path('hhee/filter/', FiltroHHEEListView.as_view(), name='filtrohhee'),
], 'hhee')