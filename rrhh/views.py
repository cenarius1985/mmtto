from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import rrhh
from django.db.models import Q
from .forms import RRHHForm, RRHHForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class RRHHListView(ListView):
    model = rrhh
    paginate_by = 50

class RRHHDetailView(DetailView):
    model = rrhh

@method_decorator(staff_member_required, name='dispatch')
class RRHHCreate(CreateView):
    model = rrhh
    form_class = RRHHForm
    success_url = reverse_lazy('rrhh:rrhh')

@method_decorator(staff_member_required, name='dispatch')
class RRHHUpdate(UpdateView):
    model = rrhh
    form_class = RRHHForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('rrhh:updaterrhh', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class RRHHDelete(DeleteView):
    model = rrhh
    success_url = reverse_lazy('rrhh:rrhh')

class FiltroRRHHListView(ListView):
    model = rrhh
    template_name= 'rrhh/rrhh_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return rrhh.objects.all()[:50]
        else:
            queryset =rrhh.objects.filter(Q(nombres__icontains=filter_val)| Q(apellidos__icontains=filter_val)| Q(cargo__icontains=filter_val)
            | Q(estado__icontains=filter_val) | Q(unidad__icontains=filter_val)| Q(funcion__icontains=filter_val) | Q(contrato__icontains=filter_val)
            )
            
            return queryset[:50]
    
    
   
   