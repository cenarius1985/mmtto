from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Capacitacion
from django.db.models import Q
from .forms import CapacitacionForm, CapacitacionForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class CapacitacionListView(ListView):
    model = Capacitacion
    paginate_by = 50

class CursoTemplateView(TemplateView):
    template_name = "capacitacion/curso.html"
   
class CapacitacionDetailView(DetailView):
    model = Capacitacion

@method_decorator(staff_member_required, name='dispatch')
class CapacitacionCreate(CreateView):
    model = Capacitacion
    form_class = CapacitacionForm
    success_url = reverse_lazy('capacitacion:capacitacion')

@method_decorator(staff_member_required, name='dispatch')
class CapacitacionUpdate(UpdateView):
    model = Capacitacion
    form_class = CapacitacionForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('capacitacion:updatecapacitacion', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class CapacitacionDelete(DeleteView):
    model = Capacitacion
    success_url = reverse_lazy('capacitacion:capacitacion')
######################################CURSOS########################################################
class FiltroExcelListView(ListView):
    model = Capacitacion
    template_name= 'capacitacion/capacitacion_list.html'
    def get_queryset(self):
        queryset= Capacitacion.objects.filter(Q(nombre ='excel'))
        return queryset

class FiltroCapsulaListView(ListView):
    model = Capacitacion
    template_name= 'capacitacion/capacitacion_list.html'
    def get_queryset(self):
        queryset= Capacitacion.objects.filter(Q(nombre ='capsula'))
        return queryset

class FiltroEdanx12ListView(ListView):
    model = Capacitacion
    template_name = 'capacitacion/capacitacion_list.html'
    def get_queryset(self):
        queryset = Capacitacion.objects.filter(Q(nombre='Monitor X12'))
        return queryset

class FiltroAirvo2ListView(ListView):
    model = Capacitacion
    template_name = 'capacitacion/capacitacion_list.html'
    def get_queryset(self):
        queryset = Capacitacion.objects.filter(Q(nombre='AIRVO2'))
        return queryset

class FiltroTrilogy2ListView(ListView):
    model = Capacitacion
    template_name = 'capacitacion/capacitacion_list.html'
    def get_queryset(self):
        queryset = Capacitacion.objects.filter(Q(nombre='Ventilador Trilogy EVO'))
        return queryset

class ExtintoresListView(ListView):
    model = Capacitacion
    template_name = 'capacitacion/capacitacion_list.html'
    def get_queryset(self):
        queryset = Capacitacion.objects.filter(Q(nombre='Uso de Extintores'))
        return queryset
