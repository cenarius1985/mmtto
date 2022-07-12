from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import proveedores
from django.db.models import Q
from .forms import ProveedoresForm, ProveedoresForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ProveedoresListView(ListView):
    model = proveedores
    paginate_by = 50

class ProveedoresDetailView(DetailView):
    model = proveedores

@method_decorator(staff_member_required, name='dispatch')
class ProveedoresCreate(CreateView):
    model = proveedores
    form_class = ProveedoresForm
    success_url = reverse_lazy('proveedores:proveedores')

@method_decorator(staff_member_required, name='dispatch')
class ProveedoresUpdate(UpdateView):
    model = proveedores
    form_class = ProveedoresForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('proveedores:updateproveedores', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ProveedoresDelete(DeleteView):
    model = proveedores
    success_url = reverse_lazy('proveedores:proveedores')

class FiltroProveedoresListView(ListView):
    model = proveedores
    template_name= 'proveedores/proveedores_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return proveedores.objects.all()[:50]
        else:
            queryset =proveedores.objects.filter(Q(numerofactura__icontains=filter_val)| Q(fecha__icontains=filter_val)| Q(proveedor__icontains=filter_val)
            | Q(numeroordencompra__icontains=filter_val) | Q(estadofactura__icontains=filter_val)| Q(fechaemision__icontains=filter_val)| Q(servicio__icontains=filter_val)
            | Q(detalle__icontains=filter_val)
            
            )
            
            return queryset[:50]
