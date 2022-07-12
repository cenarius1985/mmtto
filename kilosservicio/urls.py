from django.urls import path
from .views import KilosservicioDelete, KilosservicioCreate, KilosservicioDetailView,KilosservicioUpdate, KilosservicioListView, FiltroKilosservicioListView

kilosservicio_patterns = ([
    path('kilosservicio/', KilosservicioListView.as_view(), name='kilosservicio'),
    path('kilosservicio/<int:pk>/', KilosservicioDetailView.as_view(), name='detailkilosservicio'),
    path('create/kilosservicio', KilosservicioCreate.as_view(), name='createkilosservicio'),
    path('kilosservicio/update/<int:pk>/', KilosservicioUpdate.as_view(), name='updatekilosservicio'),
    path('kilosservicio/delete/<int:pk>/', KilosservicioDelete.as_view(), name='deletekilosservicio'),
    path('kilosservicio/filter/', FiltroKilosservicioListView.as_view(), name='filtrokilosservicio'),
], 'kilosservicio')