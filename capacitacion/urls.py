from django.urls import path
from .views import CapacitacionDelete, CapacitacionCreate, CapacitacionDetailView,CapacitacionUpdate, CapacitacionListView, FiltroExcelListView, CursoTemplateView
from .views import FiltroCapsulaListView, FiltroEdanx12ListView,FiltroAirvo2ListView, FiltroTrilogy2ListView, ExtintoresListView

capacitacion_patterns = ([
    path('capacitacion/', CapacitacionListView.as_view(), name='capacitacion'),
    path('capacitacion/<int:pk>/', CapacitacionDetailView.as_view(), name='detailcapacitacion'),
    path('create/capacitacion', CapacitacionCreate.as_view(), name='createcapacitacion'),
    path('capacitacion/update/<int:pk>/', CapacitacionUpdate.as_view(), name='updatecapacitacion'),
    path('capacitacion/delete/<int:pk>/', CapacitacionDelete.as_view(), name='deletecapacitacion'),
    path('capacitacion/curso/', CursoTemplateView.as_view(), name='cursotemplate'),
##############################Cursos#################################################
    path('capacitacion/excel/', FiltroExcelListView.as_view(), name='excel'),
    path('capacitacion/capsula/', FiltroCapsulaListView.as_view(), name='capsula'),
    path('capacitacion/edanx12/', FiltroEdanx12ListView.as_view(), name='edanx12'),
    path('capacitacion/airvo2/', FiltroAirvo2ListView.as_view(), name='airvo2'),
    path('capacitacion/trilogy/', FiltroTrilogy2ListView.as_view(), name='trilogy'),
     path('capacitacion/extintores/', ExtintoresListView.as_view(), name='extintores'),
   
], 'capacitacion')

