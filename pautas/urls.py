from django.urls import path
from .views import PautasView, CriticosView, EstanqueAguaCreate, EstanqueAguaDetailView, InfraestructuraView, CalefaccionCentralizadaCreate 
from .views import CalefaccionCentralizadaDetailView, TechumbreCreate, TechumbreDetailView, AspiracionCreate, AspiracionDetailView, GasesCreate
from .views import GasesDetailView, MontacargaCreate, MontacargaDetailView, GeneralCreate, GeneralDetailView, GeneralView, IndustrialView, IluminacionCreate
from .views import IluminacionDetailView, AltaDetailView, AltaCreate, BajaCreate, BajaDetailView, FueraCreate, FueraDetailView, ReingresoCreate, ReingresoDetailView, ComodatoCreate, ComodatoDetailView
from .views import CovidMonitorCreate, CovidMonitorDetailView, CovidVentiladorCreate, CovidVentiladorDetailView

pautas_patterns = ([
    path('pautas/mmtto/', PautasView.as_view(), name='pautas'),
    path('pautas/criticos/', CriticosView.as_view(), name='criticos'),
    path('pautas/infraestructura/', InfraestructuraView.as_view(), name='infraestructura'),
    path('pautas/relevantes/', GeneralView.as_view(), name='general'),
    path('pautas/industrial/', IndustrialView.as_view(), name='industrial'),
    ##path de pautas de estanques de agua###
    path('pautas/estanqueagua/<int:pk>/', EstanqueAguaDetailView.as_view(), name='estanqueaguadetail'),
    path('pautas/estanqueagua/', EstanqueAguaCreate.as_view(), name='estanqueaguacreate'),
    ##path de pautas de calefaccion centralizada###
    path('pautas/calefaccion/<int:pk>/', CalefaccionCentralizadaDetailView.as_view(), name='calefacciondetail'),
    path('pautas/calefaccion/', CalefaccionCentralizadaCreate.as_view(), name='calefaccioncreate'),
    ##path de techumbre###
    path('pautas/techumbre/<int:pk>/', TechumbreDetailView.as_view(), name='techumbredetail'),
    path('pautas/techumbre/', TechumbreCreate.as_view(), name='techumbrecreate'),
    ##path de Sistema de Aspiracion Centralizado###
    path('pautas/aspiracion/<int:pk>/', AspiracionDetailView.as_view(), name='aspiraciondetail'),
    path('pautas/aspiracion/', AspiracionCreate.as_view(), name='aspiracioncreate'),
    ##path de Sistema de Gases Centralizado###
    path('pautas/gases/<int:pk>/', GasesDetailView.as_view(), name='gasesdetail'),
    path('pautas/gases/', GasesCreate.as_view(), name='gasescreate'),
    ##path de Sistema de Gases Centralizado###
    path('pautas/montacarga/<int:pk>/', MontacargaDetailView.as_view(), name='montacargadetail'),
    path('pautas/montacarga/', MontacargaCreate.as_view(), name='montacargacreate'),
    ##path Pauta General###
    path('pautas/general/<int:pk>/', GeneralDetailView.as_view(), name='generaldetail'),
    path('pautas/general/', GeneralCreate.as_view(), name='generalcreate'),
    ##path Pauta de Iluminacion###
    path('pautas/iluminacion/<int:pk>/', IluminacionDetailView.as_view(), name='iluminaciondetail'),
    path('pautas/iluminacion/', IluminacionCreate.as_view(), name='iluminacioncreate'),
    ##path Pauta de Alta de Equipos###
    path('pautas/alta/<int:pk>/', AltaDetailView.as_view(), name='altadetail'),
    path('pautas/alta/', AltaCreate.as_view(), name='altacreate'),
    ##path Pauta de Baja de Equipos###
    path('pautas/baja/<int:pk>/', BajaDetailView.as_view(), name='bajadetail'),
    path('pautas/baja/', BajaCreate.as_view(), name='bajacreate'),
     ##path Pauta de Equipo Fuera de Servicio###
    path('pautas/fuera/<int:pk>/', FueraDetailView.as_view(), name='fueradetail'),
    path('pautas/fuera/', FueraCreate.as_view(), name='fueracreate'),
     ##path Pauta de Reingreso Fuera de Servicio###
    path('pautas/reingreso/<int:pk>/', ReingresoDetailView.as_view(), name='reingresodetail'),
    path('pautas/reingreso/', ReingresoCreate.as_view(), name='reingresocreate'),
    ##path Pauta de Iluminacion###
    path('pautas/comodato/<int:pk>/', ComodatoDetailView.as_view(), name='comodatodetail'),
    path('pautas/comodato/', ComodatoCreate.as_view(), name='comodatocreate'),
    path('pautas/covid/monitor/<int:pk>/', CovidMonitorDetailView.as_view(), name='covidmonitordetail'),
    path('pautas/covid/Monitor', CovidMonitorCreate.as_view(), name='covidmonitorcreate'),
    path('pautas/covid/ventilador/<int:pk>/', CovidVentiladorDetailView.as_view(), name='covidventiladordetail'),
    path('pautas/covid/ventilador', CovidVentiladorCreate.as_view(), name='covidventiladorcreate'),
], 'pautas')