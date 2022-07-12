from django.shortcuts import render
from excel_response import ExcelView

from inventario.models import inventario
from actas.models import actas
from clima.models import clima
from comunes.models import comunes
from costos.models import costos
from externo.models import MantenimientoExterno
from facturaroperia.models import facturaroperia
from industriales.models import industriales
from infraestructura.models import infraestructura
from kilosservicio.models import kilosservicio
from licitacion.models import licitacion
from monitoreo.models import monitoreo
from ordenes.models import ordenes
from ordenestalleres.models import ordenestalleres
from otautomotriz.models import otautomotriz
from proveedores.models import proveedores
from ropaexterno.models import ropaexterno
from roperiaconfeccion.models import roperiaconfeccion
from rrhh.models import rrhh
from solicitudes.models import solicitudes
from solicitudestalleresabas.models import solicitudestalleresabas
from ssgg.models import cartola, moviles
from ambulancia.models import ParqueAutomotriz
from colisiones.models import colisiones
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from informe.models import Informes
from justificacion.models import Justificacion
from control.models import Control
from guia.models import Guia
from covid.models import covid
from hhee.models import  hhee
from ambiente.models import ambiente


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class GuiaView(ExcelView):
    model = Guia

class InventarioView(ExcelView):
    model = inventario

class ControlView(ExcelView):
    model = Control

class InformesView(ExcelView):
    model = Informes

class JustificacionView(ExcelView):
    model = Justificacion

class ActasView(ExcelView):
    model = actas

class ClimaView(ExcelView):
    model = clima

class ComunesView(ExcelView):
    model = comunes

class CostosView(ExcelView):
    model = costos

class ExternoView(ExcelView):
    model = MantenimientoExterno

class FacturaRoperiaView(ExcelView):
    model = facturaroperia

class IndustrialesView(ExcelView):
    model = industriales

class InfraestructuraView(ExcelView):
    model = infraestructura

class KilosServicioView(ExcelView):
    model = kilosservicio

class LicitacionView(ExcelView):
    model = licitacion

class MonitoreoView(ExcelView):
    model = monitoreo

class OrdenesView(ExcelView):
    model = ordenes

class OrdenesTalleresView(ExcelView):
    model = ordenestalleres

class OtAutomotrizView(ExcelView):
    model = otautomotriz

class ProveedoresView(ExcelView):
    model = proveedores

class RopaExternoView(ExcelView):
    model = ropaexterno

class RoperiaConfeccionView(ExcelView):
    model = roperiaconfeccion

class RrhhView(ExcelView):
    model = rrhh

class SolicitudesView(ExcelView):
    model = solicitudes

class SolicitudesTalleresAbasView(ExcelView):
    model = solicitudestalleresabas

class CartolaView(ExcelView):
    model = cartola

class MovilesView(ExcelView):
    model = moviles

class ParqueAutomotrizView(ExcelView):
    model = ParqueAutomotriz

class CovidView(ExcelView):
    model = covid

class HHEEView(ExcelView):
    model = hhee
class AmbienteView(ExcelView):
    model = ambiente
@method_decorator(staff_member_required, name='dispatch')
class ColisionesView(ExcelView):
    model = colisiones