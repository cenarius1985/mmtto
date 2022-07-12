from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from monitoreo.models import monitoreo
from monitoreo.forms import MonitoreoForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

class PautasView(TemplateView):

    template_name = "pautas/pautas.html"

class CriticosView(TemplateView):
    
    template_name = "pautas/criticos.html"

class InfraestructuraView(TemplateView):
    
    template_name = "pautas/infraestructura.html"

class GeneralView(TemplateView):
    
    template_name = "pautas/general.html"

class IndustrialView(TemplateView):
    
    template_name = "pautas/industrial.html"


###########Pauta de Estanques de agua Potable##################


@method_decorator(staff_member_required, name='dispatch')
class EstanqueAguaCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/estanqueagua_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Estanque de Agua Potable'
        form.instance.save()
        return response

class EstanqueAguaDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/estanqueagua_detail.html'

###########Fin Pauta de Estanques de agua Potable####
###########Calefaccion Centralizada##################
@method_decorator(staff_member_required, name='dispatch')
class CalefaccionCentralizadaCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/calefaccioncentralizada_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Calefaccion Centralizada'
        form.instance.save()
        return response

class CalefaccionCentralizadaDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/calefaccioncentralizada_detail.html'

###########Fin Calefaccion Centralizada##################
###########Techumbre#####################################
@method_decorator(staff_member_required, name='dispatch')
class TechumbreCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/techumbre_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Techumbre'
        form.instance.tecnico1=''
        form.instance.save()
        return response

class TechumbreDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/techumbre_detail.html'

###########Fin Techumbre##################
###########ASPIRACION CENTRALIZADO########
@method_decorator(staff_member_required, name='dispatch')
class AspiracionCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/aspiracion_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Sistema de Aspiracion Centralizado'
        form.instance.save()
        return response

class AspiracionDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/aspiracion_detail.html'

###########Fin Techumbre##################
###########GASES CENTRALIZADOS########
@method_decorator(staff_member_required, name='dispatch')
class GasesCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/gases_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Sistema de Gases Clinicos Centralizados'
        form.instance.save()
        return response

class GasesDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/gases_detail.html'

###########Fin GASES CENTRALIZADOS##################
###########Inicio Montacarga########################
@method_decorator(staff_member_required, name='dispatch')
class MontacargaCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/montacarga_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Sistema de Transporte Vertical'
        form.instance.save()
        return response

class MontacargaDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/montacarga_detail.html'
###########Fin Montacarga########################
###########Inicio Pauta General########################
@method_decorator(staff_member_required, name='dispatch')
class GeneralCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/general_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')

class GeneralDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/general_detail.html'
###########Pauta General########################
###########Inicio Pauta Iluminacion########################
@method_decorator(staff_member_required, name='dispatch')
class IluminacionCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/iluminacion_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Sistema de Iluminacion'
        form.instance.save()
        return response

class IluminacionDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/iluminacion_detail.html'
###########Pauta Alta de equipos########################
@method_decorator(staff_member_required, name='dispatch')
class AltaCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/alta_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.tecnico1='Alta de Equipos'
        form.instance.save()
        return response

class AltaDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/alta_detail.html'
###########Pauta Fin Alta########################
###########Pauta Baja de equipos########################
@method_decorator(staff_member_required, name='dispatch')
class BajaCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/baja_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.tecnico1='Baja de Equipos'
        form.instance.save()
        return response

class BajaDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/baja_detail.html'
###########Pauta Fin Baja########################
###########Pauta Fuera de Servicio de equipos########################
@method_decorator(staff_member_required, name='dispatch')
class FueraCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/fuera_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.tecnico1='Equipo Fuera de Servicio'
        form.instance.save()
        return response

class FueraDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/fuera_detail.html'
###########Pauta Fin ########################
###########Pauta Reingreso de equipos########################
@method_decorator(staff_member_required, name='dispatch')
class ReingresoCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/reingreso_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.tecnico1='Reingreso de Equipo Fuera de Servicio'
        form.instance.save()
        return response

class ReingresoDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/reingreso_detail.html'
###########Pauta Fin########################
###########Pauta COMODATO########################
@method_decorator(staff_member_required, name='dispatch')
class ComodatoCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/comodato_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.tecnico1='COMODATO o ARRIENDO'
        form.instance.save()
        return response

class ComodatoDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/comodato_detail.html'

###########FIN Pauta COMODATO########################
###########Pautas COVID########################
#########monitoreo Hemodinamico####################
@method_decorator(staff_member_required, name='dispatch')
class CovidMonitorCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/covid_monitor_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.tecnico1='COVID-19 Monitoreo'
        form.instance.save()
        return response

class CovidMonitorDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/covid_monitor_detail.html'
########### Ventiladores Mecanicos###################
@method_decorator(staff_member_required, name='dispatch')
class CovidVentiladorCreate(CreateView):
    model = monitoreo
    template_name = 'pautas/covid_ventilador_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.tecnico1='COVID-19 ventilador'
        form.instance.save()
        return response

class CovidVentiladorDetailView(DetailView):
    model = monitoreo
    template_name = 'pautas/covid_ventilador_detail.html'

###########Fin COVID########################