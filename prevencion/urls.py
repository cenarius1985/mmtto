from django.urls import path
from .views import PrevencionDelete, PrevencionCreate, PrevencionDetailView,PrevencionUpdate, PrevencionListView, FiltroPrevencionListView

prevencion_patterns = ([
    path('prevencion/', PrevencionListView.as_view(), name='prevencion'),
    path('prevencion/<int:pk>/', PrevencionDetailView.as_view(), name='detailprevencion'),
    path('create/prevencion', PrevencionCreate.as_view(), name='createprevencion'),
    path('prevencion/update/<int:pk>/', PrevencionUpdate.as_view(), name='updateprevencion'),
    path('prevencion/delete/<int:pk>/', PrevencionDelete.as_view(), name='deleteprevencion'),
    path('prevencion/filter/', FiltroPrevencionListView.as_view(), name='filtroprevencion'),
], 'prevencion')