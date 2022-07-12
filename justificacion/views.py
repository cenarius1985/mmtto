from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Justificacion
from django.db.models import Q
from .forms import JustificacionForm, JustificacionForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class JustificacionListView(ListView):
    model = Justificacion
    paginate_by = 50
    
class JustificacionDetailView(DetailView):
    model = Justificacion

@method_decorator(staff_member_required, name='dispatch')
class JustificacionCreate(CreateView):
    model = Justificacion
    form_class = JustificacionForm
    success_url = reverse_lazy('justificacion:justificacion')

@method_decorator(staff_member_required, name='dispatch')
class JustificacionUpdate(UpdateView):
    model = Justificacion
    form_class = JustificacionForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('justificacion:updatejustificacion', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class JustificacionDelete(DeleteView):
    model = Justificacion
    success_url = reverse_lazy('justificacion:justificacion')

class FiltroJustificacionListView(ListView):
    model = Justificacion
    template_name= 'informe/justificacion_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return Justificacion.objects.all()[:50]
        else:
            queryset =Justificacion.objects.filter(Q(nombre__icontains=filter_val)| Q(servicio__icontains=filter_val) )
            
            return queryset[:50]
    
    
   