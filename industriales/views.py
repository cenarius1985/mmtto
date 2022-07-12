from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import industriales
from django.db.models import Q
from .forms import IndustrialesForm, IndustrialesForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class IndustrialesListView(ListView):
    model = industriales
    paginate_by = 50

class IndustrialesDetailView(DetailView):
    model = industriales

@method_decorator(staff_member_required, name='dispatch')
class IndustrialesCreate(CreateView):
    model = industriales
    form_class = IndustrialesForm
    success_url = reverse_lazy('industriales:industriales')

@method_decorator(staff_member_required, name='dispatch')
class IndustrialesUpdate(UpdateView):
    model = industriales
    form_class = IndustrialesForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('industriales:updateindustriales', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class IndustrialesDelete(DeleteView):
    model = industriales
    success_url = reverse_lazy('industriales:industriales')

class FiltroIndustrialesListView(ListView):
    model = industriales
    template_name= 'industriales/industriales_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return industriales.objects.all()[:50]
        else:
            queryset =industriales.objects.filter(Q(Nombre_Equipo__icontains=filter_val)| Q(Marca__icontains=filter_val)| Q(Modelo__icontains=filter_val)
            | Q(Serie__icontains=filter_val) | Q(Numero_Inventario__icontains=filter_val)| Q(Vida_Util__icontains=filter_val)| Q(Condicion__icontains=filter_val)
            | Q(Instalacion__icontains=filter_val)| Q(Frecuencia__icontains=filter_val)| Q(Estado__icontains=filter_val)| Q(Servicio_Clinico__icontains=filter_val)
            )
            
            return queryset[:50]
