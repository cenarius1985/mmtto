from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import ropaexterno
from django.db.models import Q
from .forms import RopaexternoForm, RopaexternoForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class RopaexternoListView(ListView):
    model = ropaexterno
    paginate_by = 50

class RopaexternoDetailView(DetailView):
    model = ropaexterno

@method_decorator(staff_member_required, name='dispatch')
class RopaexternoCreate(CreateView):
    model = ropaexterno
    form_class = RopaexternoForm
    success_url = reverse_lazy('ropaexterno:ropaexterno')

@method_decorator(staff_member_required, name='dispatch')
class RopaexternoUpdate(UpdateView):
    model = ropaexterno
    form_class = RopaexternoForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ropaexterno:updateropaexterno', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class RopaexternoDelete(DeleteView):
    model = ropaexterno
    success_url = reverse_lazy('ropaexterno:ropaexterno')

class FiltroRopaexternoListView(ListView):
    model = ropaexterno
    template_name= 'ropaexterno/ropaexterno_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return ropaexterno.objects.all()[:50]
        else:
            queryset =ropaexterno.objects.filter(Q(Nombre_Empresa__icontains=filter_val)| Q(Guia__icontains=filter_val)| Q(Fecha__icontains=filter_val)
            | Q(Detalle__icontains=filter_val) | Q(Cantidad__icontains=filter_val)
            )
            
            return queryset[:50]