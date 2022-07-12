from django.urls import path
from .views import SolicitudesDelete, SolicitudesCreate, SolicitudesDetailView,SolicitudesUpdate, SolicitudesListView, FiltroSolicitudesListView

solicitudes_patterns = ([
    path('solicitudes/', SolicitudesListView.as_view(), name='solicitudes'),
    path('solicitudes/<int:pk>/', SolicitudesDetailView.as_view(), name='detailsolicitudes'),
    path('create/solicitudes', SolicitudesCreate.as_view(), name='createsolicitudes'),
    path('solicitudes/update/<int:pk>/', SolicitudesUpdate.as_view(), name='updatesolicitudes'),
    path('solicitudes/delete/<int:pk>/', SolicitudesDelete.as_view(), name='deletesolicitudes'),
    path('solicitudes/filter/', FiltroSolicitudesListView.as_view(), name='filtrosolicitudes'),
], 'solicitudes')