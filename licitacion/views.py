from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import licitacion
from django.db.models import Q
from .forms import LicitacionForm, LicitacionForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class LicitacionListView(ListView):
    model = licitacion
    paginate_by = 50

class LicitacionDetailView(DetailView):
    model = licitacion

@method_decorator(staff_member_required, name='dispatch')
class LicitacionCreate(CreateView):
    model = licitacion
    form_class = LicitacionForm
    success_url = reverse_lazy('licitacion:licitacion')

@method_decorator(staff_member_required, name='dispatch')
class LicitacionUpdate(UpdateView):
    model = licitacion
    form_class = LicitacionForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('licitacion:updatelicitacion', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class LicitacionDelete(DeleteView):
    model = licitacion
    success_url = reverse_lazy('licitacion:licitacion')

class FiltroLicitacionListView(ListView):
    model = licitacion
    template_name= 'licitacion/licitacion_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return licitacion.objects.all()[:50]
        else:
            queryset =licitacion.objects.filter(Q(Nombre__icontains=filter_val)| Q(detalle__icontains=filter_val)| Q(ID_Mercado_Publico__icontains=filter_val)
            | Q(estadolicitacion__icontains=filter_val) | Q(adjudicado__icontains=filter_val)| Q(observaciones__icontains=filter_val)
            | Q(detalle__icontains=filter_val)
            
            )
            
            return queryset[:50]