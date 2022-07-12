from django.urls import path
from .views import  MonitoreoListView, MonitoreoCreate, MonitoreoDetailView,FiltroMonitoreoListView, MonitoreoUpdate, MonitoreoDelete

monitores_patterns = ([
    path('', MonitoreoListView.as_view(), name='monitores'),
    path('inventario_filter/', FiltroMonitoreoListView.as_view(), name='filtroinventario'),
    path('create_monitor/', MonitoreoCreate.as_view(), name='create1'),
    path('<int:pk>/<slug:slug>/', MonitoreoDetailView.as_view(), name='monitor'),
    path('monitoreo/update/<int:pk>/', MonitoreoUpdate.as_view(), name='monitoreoupdate'),
    path('delete/monitoreo/<int:pk>/', MonitoreoDelete.as_view(), name='deletemonitoreo'),
], 'monitores')