from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Manuales
from django.db.models import Q
from .forms import ManualesForm, ManualesForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ManualesListView(ListView):
    model = Manuales
    paginate_by = 50
    
class ManualesDetailView(DetailView):
    model = Manuales

@method_decorator(staff_member_required, name='dispatch')
class ManualesCreate(CreateView):
    model = Manuales
    form_class = ManualesForm
    success_url = reverse_lazy('manuales:manuales')

@method_decorator(staff_member_required, name='dispatch')
class ManualesUpdate(UpdateView):
    model = Manuales
    form_class = ManualesForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('manuales:updatemanuales', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ManualesDelete(DeleteView):
    model = Manuales
    success_url = reverse_lazy('manuales:manuales')

class FiltroManualesListView(ListView):
    model = Manuales
    template_name= 'informe/manuales_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return Manuales.objects.all()[:50]
        else:
            queryset =Manuales.objects.filter(Q(nombre__icontains=filter_val)| Q(marca__icontains=filter_val)| Q(modelo__icontains=filter_val) )
            
            return queryset[:50]
    
    
   