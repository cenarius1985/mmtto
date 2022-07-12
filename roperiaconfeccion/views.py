from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import roperiaconfeccion
from django.db.models import Q
from .forms import RoperiaconfeccionForm, RoperiaconfeccionForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class RoperiaconfeccionListView(ListView):
    model = roperiaconfeccion
    paginate_by = 50

class RoperiaconfeccionDetailView(DetailView):
    model = roperiaconfeccion

@method_decorator(staff_member_required, name='dispatch')
class RoperiaconfeccionCreate(CreateView):
    model = roperiaconfeccion
    form_class = RoperiaconfeccionForm
    success_url = reverse_lazy('roperiaconfeccion:roperiaconfeccion')

@method_decorator(staff_member_required, name='dispatch')
class RoperiaconfeccionUpdate(UpdateView):
    model = roperiaconfeccion
    form_class = RoperiaconfeccionForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('roperiaconfeccion:updateroperiaconfeccion', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class RoperiaconfeccionDelete(DeleteView):
    model = roperiaconfeccion
    success_url = reverse_lazy('roperiaconfeccion:roperiaconfeccion')

class FiltroRoperiaconfeccionListView(ListView):
    model = roperiaconfeccion
    template_name= 'roperiaconfeccion/roperiaconfeccion_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return roperiaconfeccion.objects.all()[:50]
        else:
            queryset =roperiaconfeccion.objects.filter(Q(Fecha_OC__icontains=filter_val)| Q(Numero_Boleta__icontains=filter_val)| Q(RUT__icontains=filter_val)
            | Q(Nombre_Empresa__icontains=filter_val) | Q(Detalle__icontains=filter_val)| Q(OC__icontains=filter_val)
            )
            
            return queryset[:50]