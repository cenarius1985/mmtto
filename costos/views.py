from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import costos
from django.db.models import Q
from .forms import CostosForm, CostosForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class CostosListView(ListView):
    model = costos
    paginate_by = 50

class CostosDetailView(DetailView):
    model = costos

@method_decorator(staff_member_required, name='dispatch')
class CostosCreate(CreateView):
    model = costos
    form_class = CostosForm
    success_url = reverse_lazy('costos:costos')

@method_decorator(staff_member_required, name='dispatch')
class CostosUpdate(UpdateView):
    model = costos
    form_class = CostosForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('costos:updatecostos', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class CostosDelete(DeleteView):
    model = costos
    success_url = reverse_lazy('costos:costos')

class FiltroCostosListView(ListView):
    model = costos
    template_name= 'costos/costos_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return costos.objects.all()[:50]
        else:
            queryset =costos.objects.filter(Q(proveedor__icontains=filter_val)| Q(fechae__icontains=filter_val)| Q(detalle__icontains=filter_val)
            | Q(criticorelevante__icontains=filter_val) | Q(serviciosolicita__icontains=filter_val)| Q(numerofactura__icontains=filter_val)
            | Q(convenio__icontains=filter_val)| Q(numerolicitacion__icontains=filter_val)| Q(numeroordencompra__icontains=filter_val)
            | Q(observaciones__icontains=filter_val)| Q(mantenimiento__icontains=filter_val)
            )
            
            return queryset[:50]
