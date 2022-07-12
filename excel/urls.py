from django.urls import path

from .views import InventarioView, ActasView, ClimaView, ComunesView, CostosView 
from .views import ExternoView, FacturaRoperiaView, IndustrialesView, InfraestructuraView, KilosServicioView
from .views import LicitacionView, MonitoreoView, OrdenesView, OrdenesTalleresView, OtAutomotrizView, RopaExternoView
from .views import RoperiaConfeccionView, RrhhView,SolicitudesView,SolicitudesTalleresAbasView,CartolaView, MovilesView 
from .views import ParqueAutomotrizView, ColisionesView, ProveedoresView, InformesView, JustificacionView, ControlView
from .views import GuiaView, CovidView, HHEEView, AmbienteView


urlpatterns = [
    path('inventario/',InventarioView.as_view(), name='inventarioexcel'),
    path('actas/',ActasView.as_view(), name='actasexcel'),
    path('clima/',ClimaView.as_view(), name='climaexcel'),
    path('comunes/',ComunesView.as_view(), name='comunesexcel'),
    path('costos/',CostosView.as_view(), name='costosexcel'),
    path('externo/',ExternoView.as_view(), name='externoexcel'),
    path('facturaroperia/',FacturaRoperiaView.as_view(), name='facturaroperiaexcel'),
    path('industriales/',IndustrialesView.as_view(), name='industrialesexcel'),
    path('infraestructura/',InfraestructuraView.as_view(), name='infraestructuraexcel'),
    path('kilos/servicio/',KilosServicioView.as_view(), name='kilosservicioexcel'),
    path('licitacion/',LicitacionView.as_view(), name='licitacionexcel'),
    path('monitoreo/',MonitoreoView.as_view(), name='monitoreoexcel'),
    path('ordenes/',OrdenesView.as_view(), name='ordenesexcel'),
    path('ordenestalleres/',OrdenesTalleresView.as_view(), name='ordenestalleresexcel'),
    path('otautomotriz/',OtAutomotrizView.as_view(), name='otautomotrizexcel'),
    path('proveedores/', ProveedoresView.as_view(), name='proveedoresexcel'),
    path('ropaexterno/',RopaExternoView.as_view(), name='ropaexternoexcel'),
    path('roperiaconfeccion/',RoperiaConfeccionView.as_view(), name='roperiaconfeccionexcel'),
    path('rrhh/',RrhhView.as_view(), name='rrhhexcel'),
    path('solicitudes/',SolicitudesView.as_view(), name='solicitudesexcel'),
    path('solicitudestalleresabas/',SolicitudesTalleresAbasView.as_view(), name='solicitudestalleresabasexcel'),
    path('cartolas/',CartolaView.as_view(), name='cartolaexcel'),
    path('moviles/',MovilesView.as_view(), name='movilesexcel'),
    path('parqueautomotriz/',ParqueAutomotrizView.as_view(), name='parqueautomotrizexcel'),
    path('colisiones/',ColisionesView.as_view(), name='colisionesexcel'),
    path('informes/',InformesView.as_view(), name='informesexcel'),
    path('justificacion/',JustificacionView.as_view(), name='justificacionexcel'),
    path('control/documentos/',ControlView.as_view(), name='controlexcel'),
	path('control/guia/',GuiaView.as_view(), name='guiaexcel'),
    path('control/covid/',CovidView.as_view(), name='covidexcel'),
    path('control/hhee/',HHEEView.as_view(), name='hheeexcel'),
    path('prevencion/ambiente/', AmbienteView.as_view(), name='ambienteexcel'),

]


