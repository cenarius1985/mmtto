from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import solicitudestalleresabas
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
    model = solicitudestalleresabas
    paginate_by = 50

class SolicitudesDetailView(DetailView):
    model = solicitudestalleresabas

@method_decorator(staff_member_required, name='dispatch')
class SolicitudesCreate(CreateView):
    model = solicitudestalleresabas
    form_class = SolicitudesForm
    success_url = reverse_lazy('solicitudestalleresabas:solicitudestalleresabas')

@method_decorator(staff_member_required, name='dispatch')
class SolicitudesUpdate(UpdateView):
    model = solicitudestalleresabas
    form_class = SolicitudesForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('solicitudestalleresabas:updatesolicitudestalleresabas', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class SolicitudesDelete(DeleteView):
    model = solicitudestalleresabas
    success_url = reverse_lazy('solicitudestalleresabas:solicitudestalleresabas')

class FiltroSolicitudesListView(ListView):
    model = solicitudestalleresabas
    template_name= 'solicitudestalleresabas/solicitudestalleresabas_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return solicitudestalleresabas.objects.all()[:50]
        else:
            queryset =solicitudestalleresabas.objects.filter(Q( fecha__icontains=filter_val)| Q(numeroadquisicion__icontains=filter_val)| Q(estadoOT__icontains=filter_val)
            | Q(servicioorigen__icontains=filter_val) | Q(detalle__icontains=filter_val)| Q(observaciones__icontains=filter_val)
            )
            
            return queryset[:50]