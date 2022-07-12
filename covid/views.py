from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import covid
from django.db.models import Q
from .forms import CovidForm, CovidForm2
from django.shortcuts import get_object_or_404

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
###############Filtros################################

class FiltroCovidListView(ListView):
    model = covid
    template_name= 'covid/covid_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return covid.objects.all()[:50]
        else:
            queryset =covid.objects.filter(Q(servicio__icontains=filter_val)| Q(nombre__icontains=filter_val)| Q(marca__icontains=filter_val)
            | Q(modelo__icontains=filter_val) | Q(inventario__icontains=filter_val)| Q(serie__icontains=filter_val)| Q(tecnico1__icontains=filter_val)
            )
            
            return queryset[:50]

################Termino de Filtros#######################
@method_decorator(staff_member_required, name='dispatch')
class CovidDelete(DeleteView):
    model = covid
    success_url = reverse_lazy('covid:covid')

class CovidListView(ListView):
    model = covid
    paginate_by = 50

@method_decorator(staff_member_required, name='dispatch')   
class CovidUpdate(UpdateView):
    model = covid
    form_class = CovidForm2
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('covid:covid')

###########Pautas COVID########################
#########monitoreo Hemodinamico####################
@method_decorator(staff_member_required, name='dispatch')
class CovidMonitorCreate(CreateView):
    model = covid
    template_name = 'covid/covid_monitor_form.html'
    form_class = CovidForm
    success_url = reverse_lazy('covid:covid')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.tecnico1='COVID-19 Monitoreo'
        form.instance.save()
        return response

class CovidMonitorDetailView(DetailView):
    model = covid
    template_name = 'covid/covid_monitor_detail.html'

########### Ventiladores Mecanicos###################
@method_decorator(staff_member_required, name='dispatch')
class CovidVentiladorCreate(CreateView):
    model = covid
    template_name = 'covid/covid_ventilador_form.html'
    form_class = CovidForm
    success_url = reverse_lazy('covid:covid')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.tecnico1='COVID-19 ventilador'
        form.instance.save()
        return response

class CovidVentiladorDetailView(DetailView):
    model = covid
    template_name = 'covid/covid_ventilador_detail.html'

###########Fin COVID########################