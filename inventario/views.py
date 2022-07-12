from django.shortcuts import render
from .models import inventario
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from monitoreo.models import monitoreo
from .forms import InventarioForm
from .forms import InventarioForm2
from django.views.generic import TemplateView
from django.db.models import Sum
import datetime


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class InventarioListView(ListView):
    model = inventario
    paginate_by = 50
    def get_queryset(self):
        ahora=int(datetime.date.today().year)
        queryset= inventario.objects.annotate(total=(Sum('vida_util')+Sum('ano'))-ahora)
        return queryset

    
class InventarioDetailView(DetailView):
    model = inventario

@method_decorator(staff_member_required, name='dispatch')   
class InventarioUpdate(UpdateView):
    model = inventario
    form_class = InventarioForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('inventarioupdate', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class InventarioDelete(DeleteView):
    model = inventario
    success_url = reverse_lazy('inventario')


@method_decorator(staff_member_required, name='dispatch')
class InventarioCreate(CreateView):
    model = inventario
    form_class = InventarioForm
    success_url = reverse_lazy('inventario')

class FiltroInventarioListView(ListView):
    model = inventario
    template_name= 'inventario/inventario_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
             ahora=int(datetime.date.today().year)
             queryset= inventario.objects.annotate(total=(Sum('vida_util')+Sum('ano'))-ahora)
             return queryset[:50]
        else:
            ahora=int(datetime.date.today().year)
            queryset =inventario.objects.filter(
            Q(inventario__icontains=filter_val) | Q(serie__icontains=filter_val) | Q(nombre_equipo__icontains=filter_val)| Q(servicio__icontains=filter_val)| Q(critico_apoyo__icontains=filter_val)| Q(marca__icontains=filter_val)| Q(id__icontains=filter_val)
            
            ).annotate(total=(Sum('vida_util')+Sum('ano'))-ahora)
            return queryset[:50]
