from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import ambiente
from django.db.models import Q
from .forms import AmbienteForm, AmbienteForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class AmbienteListView(ListView):
    model = ambiente
    paginate_by = 50
    
class AmbienteDetailView(DetailView):
    model = ambiente

@method_decorator(staff_member_required, name='dispatch')
class AmbienteCreate(CreateView):
    model = ambiente
    form_class = AmbienteForm
    success_url = reverse_lazy('ambiente:ambiente')

@method_decorator(staff_member_required, name='dispatch')
class AmbienteUpdate(UpdateView):
    model = ambiente
    form_class = AmbienteForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ambiente:updateambiente', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class AmbienteDelete(DeleteView):
    model = ambiente
    success_url = reverse_lazy('ambiente:ambiente')

class FiltroAmbienteListView(ListView):
    model = ambiente
    template_name= 'informe/ambiente_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return ambiente.objects.all()[:50]
        else:
            queryset =ambiente.objects.filter(Q(nombre__icontains=filter_val))
            
            return queryset[:50]
    
    
   