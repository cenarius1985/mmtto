from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import infraestructura
from django.db.models import Q
from .forms import InfraestructuraForm, InfraestructuraForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class InfraestructuraListView(ListView):
    model = infraestructura
    paginate_by = 50

class InfraestructuraDetailView(DetailView):
    model = infraestructura

@method_decorator(staff_member_required, name='dispatch')
class InfraestructuraCreate(CreateView):
    model = infraestructura
    form_class = InfraestructuraForm
    success_url = reverse_lazy('infraestructura:infraestructura')

@method_decorator(staff_member_required, name='dispatch')
class InfraestructuraUpdate(UpdateView):
    model = infraestructura
    form_class = InfraestructuraForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('infraestructura:updateinfraestructura', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class InfraestructuraDelete(DeleteView):
    model = infraestructura
    success_url = reverse_lazy('infraestructura:infraestructura')

class FiltroInfraestructuraListView(ListView):
    model = infraestructura
    template_name= 'infraestructura/infraestructura_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return infraestructura.objects.all()[:50]
        else:
            queryset =infraestructura.objects.filter(Q( serviciosolicita__icontains=filter_val)| Q(fecha__icontains=filter_val)| Q(detalle__icontains=filter_val)
            | Q(numerofolio__icontains=filter_val) | Q(estadoOT__icontains=filter_val)| Q(observaciones__icontains=filter_val)
            )
            
            return queryset[:50]
