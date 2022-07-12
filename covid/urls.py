from django.urls import path
from .views import  CovidListView, CovidMonitorCreate, CovidMonitorDetailView,FiltroCovidListView, CovidUpdate, CovidDelete, CovidVentiladorDetailView, CovidVentiladorCreate

covid_patterns = ([
    path('', CovidListView.as_view(), name='covid'),
    path('inventario_filter/covid', FiltroCovidListView.as_view(), name='filtrocovid'),
    path('create_monitor/covid', CovidMonitorCreate.as_view(), name='covidcreate'),
    path('<int:pk>/<slug:slug>/covid', CovidMonitorDetailView.as_view(), name='covidmonitor'),
    path('covid/update/<int:pk>/', CovidUpdate.as_view(), name='covidupdate'),
    path('delete/covid/<int:pk>/', CovidDelete.as_view(), name='deletecovid'),
    path('pautas/covid/monitor/<int:pk>/', CovidMonitorDetailView.as_view(), name='covidmonitordetail'),
    path('pautas/covid/Monitor', CovidMonitorCreate.as_view(), name='covidmonitorcreate'),
    path('pautas/covid/ventilador/<int:pk>/', CovidVentiladorDetailView.as_view(), name='covidventiladordetail'),
    path('pautas/covid/ventilador', CovidVentiladorCreate.as_view(), name='covidventiladorcreate'),
], 'covid')