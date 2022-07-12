from django.urls import path
from .views import JustificacionDelete, JustificacionCreate, JustificacionDetailView,JustificacionUpdate, JustificacionListView, FiltroJustificacionListView

justificacion_patterns = ([
    path('justificacion/', JustificacionListView.as_view(), name='justificacion'),
    path('justificacion/<int:pk>/', JustificacionDetailView.as_view(), name='detailjustificacion'),
    path('create/justificacion', JustificacionCreate.as_view(), name='createjustificacion'),
    path('justificacion/update/<int:pk>/', JustificacionUpdate.as_view(), name='updatejustificacion'),
    path('justificacion/delete/<int:pk>/', JustificacionDelete.as_view(), name='deletejustificacion'),
    path('justificacion/filter/', FiltroJustificacionListView.as_view(), name='filtrojustificacion'),
], 'justificacion')