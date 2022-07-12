from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import ordenestalleres
from django.db.models import Q
from .forms import OrdenestalleresForm, OrdenestalleresForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class OrdenestalleresListView(ListView):
    model = ordenestalleres
    paginate_by = 50

class OrdenestalleresDetailView(DetailView):
    model = ordenestalleres

@method_decorator(staff_member_required, name='dispatch')
class OrdenestalleresCreate(CreateView):
    model = ordenestalleres
    form_class = OrdenestalleresForm
    success_url = reverse_lazy('ordenestalleres:ordenestalleres')

@method_decorator(staff_member_required, name='dispatch')
class OrdenestalleresUpdate(UpdateView):
    model = ordenestalleres
    form_class = OrdenestalleresForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ordenestalleres:updateordenestalleres', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class OrdenestalleresDelete(DeleteView):
    model = ordenestalleres
    success_url = reverse_lazy('ordenestalleres:ordenestalleres')

class FiltroOrdenestalleresListView(ListView):
    model = ordenestalleres
    template_name= 'ordenestalleres/ordenestalleres_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return ordenestalleres.objects.all()[:50]
        else:
            queryset =ordenestalleres.objects.filter(Q( serviciosolicita__icontains=filter_val)| Q(fecha__icontains=filter_val)| Q(detalle__icontains=filter_val)
            | Q(numerofolio__icontains=filter_val) | Q(estadoOT__icontains=filter_val)| Q(observaciones__icontains=filter_val)
            )
            
            return queryset[:50]
