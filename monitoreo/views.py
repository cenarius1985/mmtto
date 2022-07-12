from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import monitoreo
from django.db.models import Q
from .forms import MonitoreoForm, MonitoreoForm2
from django.shortcuts import get_object_or_404

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)
###############Filtros################################

class FiltroMonitoreoListView(ListView):
    model = monitoreo
    template_name= 'monitoreo/monitoreo_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return monitoreo.objects.all()[:50]
        else:
            queryset =monitoreo.objects.filter(Q(servicio__icontains=filter_val)| Q(nombre__icontains=filter_val)| Q(marca__icontains=filter_val)
            | Q(modelo__icontains=filter_val) | Q(inventario__icontains=filter_val)| Q(serie__icontains=filter_val)| Q(tecnico1__icontains=filter_val)
            )
            
            return queryset[:50]


################Termino de Filtros#######################
@method_decorator(staff_member_required, name='dispatch')
class MonitoreoDelete(DeleteView):
    model = monitoreo
    success_url = reverse_lazy('monitores:monitores')

class MonitoreoListView(ListView):
    model = monitoreo
    paginate_by = 50



@method_decorator(staff_member_required, name='dispatch')
class MonitoreoCreate(CreateView):
    model = monitoreo
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Monitor Multiparametro'
        form.instance.save()
        return response
      

class MonitoreoDetailView(DetailView):
    model = monitoreo

@method_decorator(staff_member_required, name='dispatch')   
class MonitoreoUpdate(UpdateView):
    model = monitoreo
    form_class = MonitoreoForm2
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse_lazy('monitores:monitores')


