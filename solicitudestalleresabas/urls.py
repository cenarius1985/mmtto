from django.urls import path
from .views import SolicitudesDelete, SolicitudesCreate, SolicitudesDetailView,SolicitudesUpdate, SolicitudesListView, FiltroSolicitudesListView

solicitudestalleresabas_patterns = ([
    path('estado/pago/', SolicitudesListView.as_view(), name='solicitudestalleresabas'),
    path('estado/pago/<int:pk>/', SolicitudesDetailView.as_view(), name='detailsolicitudestalleresabas'),
    path('create/estado/pago/', SolicitudesCreate.as_view(), name='createsolicitudestalleresabas'),
    path('estado/pago/update/<int:pk>/', SolicitudesUpdate.as_view(), name='updatesolicitudestalleresabas'),
    path('estado/pago/delete/<int:pk>/', SolicitudesDelete.as_view(), name='deletesolicitudestalleresabas'),
    path('estado/pago/filter/', FiltroSolicitudesListView.as_view(), name='filtrosolicitudestalleresabas'),
], 'solicitudestalleresabas')