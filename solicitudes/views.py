from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import solicitudes
from django.db.models import Q
from .forms import SolicitudesForm, SolicitudesForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class SolicitudesListView(ListView):
    model = solicitudes
    paginate_by = 50

class SolicitudesDetailView(DetailView):
    model = solicitudes

@method_decorator(staff_member_required, name='dispatch')
class SolicitudesCreate(CreateView):
    model = solicitudes
    form_class = SolicitudesForm
    success_url = reverse_lazy('solicitudes:solicitudes')

@method_decorator(staff_member_required, name='dispatch')
class SolicitudesUpdate(UpdateView):
    model = solicitudes
    form_class = SolicitudesForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('solicitudes:updatesolicitudes', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class SolicitudesDelete(DeleteView):
    model = solicitudes
    success_url = reverse_lazy('solicitudes:solicitudes')

class FiltroSolicitudesListView(ListView):
    model = solicitudes
    template_name= 'solicitudes/solicitudes_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return solicitudes.objects.all()[:50]
        else:
            queryset =solicitudes.objects.filter(Q( fecha__icontains=filter_val)| Q(numeroadquisicion__icontains=filter_val)| Q(estadoOT__icontains=filter_val)
            | Q(servicioorigen__icontains=filter_val) | Q(detalle__icontains=filter_val)| Q(observaciones__icontains=filter_val)
            )
            
            return queryset[:50]