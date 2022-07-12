from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import actas
from django.db.models import Q
from .forms import ActasForm, ActasForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ActasListView(ListView):
    model = actas
    paginate_by = 50

class ActasDetailView(DetailView):
    model = actas

@method_decorator(staff_member_required, name='dispatch')
class ActasCreate(CreateView):
    model = actas
    form_class = ActasForm
    success_url = reverse_lazy('actas:actas')

@method_decorator(staff_member_required, name='dispatch')
class ActasUpdate(UpdateView):
    model = actas
    form_class = ActasForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('actas:updateactas', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ActasDelete(DeleteView):
    model = actas
    success_url = reverse_lazy('actas:actas')

class FiltroActasListView(ListView):
    model = actas
    template_name= 'actas/actas_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return actas.objects.all()[:50]
        else:
            queryset =actas.objects.filter(Q(Fecha__icontains=filter_val)| Q(serviciosolicita__icontains=filter_val)| Q(Proveedor__icontains=filter_val)
            | Q(Guia__icontains=filter_val)| Q(OC__icontains=filter_val)| Q(Licitacion__icontains=filter_val)
            )
            
            return queryset[:50]

    
