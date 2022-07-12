from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import ParqueAutomotriz
from .forms import AmbulanciaForm, AmbulanciaForm2
from django.db.models import Q

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Vistas Monitores

@method_decorator(staff_member_required, name='dispatch')
class MovilCreate(CreateView):
    model = ParqueAutomotriz
    form_class = AmbulanciaForm
    success_url = reverse_lazy('ambulancias:listaambulancia')
    

class AmbulanciaDetailView(DetailView):
    model = ParqueAutomotriz

# Create your views here.
class AmbulanciaListView(ListView):
    model = ParqueAutomotriz
    paginate_by = 50

@method_decorator(staff_member_required, name='dispatch')
class AmbulanciaDelete(DeleteView):
    model = ParqueAutomotriz
    success_url = reverse_lazy('ambulancias:listaambulancia')

@method_decorator(staff_member_required, name='dispatch')   
class AmbulanciaUpdate(UpdateView):
    model = ParqueAutomotriz
    form_class = AmbulanciaForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ambulancias:ambulanciaupdate', args=[self.object.id]) + '?ok'


class FiltroAmbulanciaListView(ListView):
    model = ParqueAutomotriz
    template_name= 'ambulancia/ParqueAutomotriz_list_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return ParqueAutomotriz.objects.all()[:50]
        else:
            queryset =ParqueAutomotriz.objects.filter(Q(Movil__icontains=filter_val)|Q(Servicio__icontains=filter_val)
            |Q(Patente__icontains=filter_val)|Q(modelo__icontains=filter_val)|Q(marca__icontains=filter_val)
            )
            
            return queryset[:50]
