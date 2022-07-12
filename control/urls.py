from django.urls import path
from .views import ControlDelete, ControlCreate, ControlDetailView,ControlUpdate, ControlListView, FiltroControlListView

control_patterns = ([
    path('control/', ControlListView.as_view(), name='control'),
    path('control/<int:pk>/', ControlDetailView.as_view(), name='detailcontrol'),
    path('create/control', ControlCreate.as_view(), name='createcontrol'),
    path('control/update/<int:pk>/', ControlUpdate.as_view(), name='updatecontrol'),
    path('control/delete/<int:pk>/', ControlDelete.as_view(), name='deletecontrol'),
    path('control/filter/', FiltroControlListView.as_view(), name='filtrocontrol'),
], 'control')