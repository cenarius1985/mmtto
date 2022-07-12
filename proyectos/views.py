from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import proyectos
from django.db.models import Q
from .forms import ProyectosForm, ProyectosForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ProyectosListView(ListView):
    model = proyectos
    paginate_by = 50

class ProyectosDetailView(DetailView):
    model = proyectos

@method_decorator(staff_member_required, name='dispatch')
class ProyectosCreate(CreateView):
    model = proyectos
    form_class = ProyectosForm
    success_url = reverse_lazy('proyectos:proyectos')

@method_decorator(staff_member_required, name='dispatch')
class ProyectosUpdate(UpdateView):
    model = proyectos
    form_class = ProyectosForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('proyectos:updateproyectos', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ProyectosDelete(DeleteView):
    model = proyectos
    success_url = reverse_lazy('proyectos:proyectos')

class FiltroProyectosListView(ListView):
    model = proyectos
    template_name= 'proyectos/proyectos_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return proyectos.objects.all()[:50]
        else:
            queryset =proyectos.objects.filter(Q(fecha__icontains=filter_val)| Q(nombre__icontains=filter_val)| Q(descripcion__icontains=filter_val))
            
            return queryset[:50]
