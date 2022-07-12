from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import facturaroperia
from django.db.models import Q
from .forms import FacturaroperiaForm, FacturaroperiaForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class FacturaroperiaListView(ListView):
    model = facturaroperia
    paginate_by = 50

class FacturaroperiaDetailView(DetailView):
    model = facturaroperia

@method_decorator(staff_member_required, name='dispatch')
class FacturaroperiaCreate(CreateView):
    model = facturaroperia
    form_class = FacturaroperiaForm
    success_url = reverse_lazy('facturaroperia:facturaroperia')

@method_decorator(staff_member_required, name='dispatch')
class FacturaroperiaUpdate(UpdateView):
    model = facturaroperia
    form_class = FacturaroperiaForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('facturaroperia:updatefacturaroperia', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class FacturaroperiaDelete(DeleteView):
    model = facturaroperia
    success_url = reverse_lazy('facturaroperia:facturaroperia')

class FiltroFacturaroperiaListView(ListView):
    model = facturaroperia
    template_name= 'facturaroperia/facturaroperia_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return facturaroperia.objects.all()[:50]
        else:
            queryset =facturaroperia.objects.filter(Q(numerofactura__icontains=filter_val)| Q(fecha__icontains=filter_val)| Q(proveedor__icontains=filter_val)
            | Q(numeroordencompra__icontains=filter_val) | Q(estadofactura__icontains=filter_val)| Q(fechaemision__icontains=filter_val)| Q(servicio__icontains=filter_val)
            | Q(detalle__icontains=filter_val)
            
            )
            
            return queryset[:50]
