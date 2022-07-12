"""mmtto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages.urls import pages_patterns
from profiles.urls import profiles_patterns
from monitoreo.urls import monitores_patterns
from oximetro.urls import oximetro_patterns
from ambulancia.urls import ambulancia_patterns
from anestesia.urls import anestesia_patterns
from desfibrilador.urls import desfibrilador_patterns
from incubadora.urls import incubadora_patterns
from ventilador.urls import ventilador_patterns
from vital.urls import vital_patterns
from ssgg.urls import cartolas_patterns
from comunes.urls import comunes_patterns
from proveedores.urls import proveedores_patterns
from licitacion.urls import licitacion_patterns
from ordenes.urls import ordenes_patterns
from infraestructura.urls import infraestructura_patterns
from otautomotriz.urls import otautomotriz_patterns
from proyectos.urls import proyectos_patterns
from rrhh.urls import rrhh_patterns
from solicitudes.urls import solicitudes_patterns
from costos.urls import costos_patterns
from clima.urls import clima_patterns
from industriales.urls import industriales_patterns
from ordenestalleres.urls import ordenestalleres_patterns
from solicitudestalleresabas.urls import solicitudestalleresabas_patterns
from roperiaconfeccion.urls import roperiaconfeccion_patterns
from ropaexterno.urls import ropaexterno_patterns
from kilosservicio.urls import kilosservicio_patterns
from facturaroperia.urls import facturaroperia_patterns
from actas.urls import actas_patterns
from pautas.urls import pautas_patterns
from colisiones.urls import colisiones_patterns
from informe.urls import informes_patterns
from gantt.urls import gantt_patterns
from justificacion.urls import justificacion_patterns
from capacitacion.urls import capacitacion_patterns
from bases.urls import bases_patterns
from control.urls import control_patterns
from ambiente.urls import ambiente_patterns
from messenger.urls import messenger_patterns
from prevencion.urls import prevencion_patterns
from guia.urls import guia_patterns
from manuales.urls import manuales_patterns
from covid.urls import covid_patterns
from hhee.urls import hhee_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mmtto/',include('core.urls')),
    path('',include('registration.urls')),
    path('',include(pages_patterns)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profiles/', include(profiles_patterns)),
    path('monitores/', include(monitores_patterns)),
    # Paths de Formulario de Oximetro de Pulso
    path('oximetro/', include(oximetro_patterns)),
    # Paths de Formulario de Ambulancia
    path('ambulancia/', include(ambulancia_patterns)),
    # Paths de Formulario de Maquinas de Anestesia
    path('anestesia/', include(anestesia_patterns)),
    # Paths de Formulario de Desfibrilador
    path('desfibrilador/', include(desfibrilador_patterns)),
    path('', include('externo.urls')),
    # Paths de Formulario de Incubadora
    path('incubadora/', include(incubadora_patterns)),
    path('', include('inventario.urls')),
    # Paths de Formulario de ventiladores
    path('ventilador/', include(ventilador_patterns)),
    # Paths de Formulario de Monitor de Signos Vitales
    path('monitor_signos_vitales/', include(vital_patterns)),
    # Paths de SSGG
    path('ssgg/', include(cartolas_patterns)),
    # Paths de Gastos Comunes
    path('gastos/comunes/', include(comunes_patterns)),
    # Paths de Gastos Comunes
    path('gastos/proveedores/', include(proveedores_patterns)),
    # Paths de Licitacion
    path('control/licitacion/', include(licitacion_patterns)),
    # Paths de ordenes de Trabajo
    path('control/ordenes/trabajo', include(ordenes_patterns)),
    # Paths de Inverntario Infraestructura
    path('inventario/infraestructura/trabajo', include(infraestructura_patterns)),
    # Paths de Oden de trabajo del Parque automotriz
    path('automotriz/parque/trabajo', include(otautomotriz_patterns)),
     # Paths de Oden de proyectos Internos
    path('proyectos/internos/trabajo', include(proyectos_patterns)),
     # Paths de RRHH
    path('trabajo/rrhh/ssgg&mmtto', include(rrhh_patterns)),
     # Paths de Solicitudes Abastecimiento
    path('trabajo/solicitudes/abastecimiento', include(solicitudes_patterns)),
     # Paths de costos de Mantenimiento
    path('trabajo/facturas/mantenimiento', include(costos_patterns)),
     # Paths de costos de Mantenimiento
    path('trabajo/clima/mantenimiento', include(clima_patterns)),
     # Paths Inventario de equipos industriales
    path('trabajo/industriales/inventario', include(industriales_patterns)),
     # Paths Ordens talleres
    path('trabajo/ordenes/talleres', include(ordenestalleres_patterns)),
    # Paths Ordens talleres
    path('abastecimiento/', include(solicitudestalleresabas_patterns)),
     # Paths Ordens de Confeccion de Ropa
    path('trabajo/roperia/corteconfeccion', include(roperiaconfeccion_patterns)),
     # Paths Envio de Ropa al extra-sistema
    path('trabajo/roperia/ropaexternalizacion', include(ropaexterno_patterns)),
     # Paths kilos por servicio
    path('trabajo/roperia/ropaservicio', include(kilosservicio_patterns)),
    # Paths Factura Roperia
    path('trabajo/roperia/factura', include(facturaroperia_patterns)),
    # Paths Actas de Equipos Medicos
    path('trabajo/Actas/equipos', include(actas_patterns)),
     # Paths excel
    path('exportar/lista/', include('excel.urls')),
     # Paths Graficos
    path('', include('graficos.urls')),
    # Paths pautas
    path('', include(pautas_patterns)),
    # Paths Colisiones
    path('', include(colisiones_patterns)),
     # Paths Gantt
    path('', include(gantt_patterns)),
    # Paths Colisiones
    path('', include(informes_patterns)),
     # Paths Justificacion
    path('', include(justificacion_patterns)),
    # Paths Capacitacion
    path('', include(capacitacion_patterns)),
      # Paths Bases
    path('', include(bases_patterns)),
    # Paths Control de Documentacion
    path('', include(control_patterns)),
    #paths grafico
    path('',include('grafico.urls')),
    # Paths de Messenger
    path('messenger/', include(messenger_patterns)),
    # Paths Control de Documentacion Prevencion
    path('', include(prevencion_patterns)),
	# Paths Control de guia
    path('', include(guia_patterns)),
      # Paths manuales de equipos
    path('', include(manuales_patterns)),
    # Paths covid
    path('mmtto/criticos/covid', include(covid_patterns)),
	 # Paths de HHEE
    path('trabajo/HHEE/MMTTO&SSGG', include(hhee_patterns)),
# Documentacion de Medio ambiente
    path('', include(ambiente_patterns)),
    

]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header="ADMINISTRADOR DE MANTENIMIENTO"
