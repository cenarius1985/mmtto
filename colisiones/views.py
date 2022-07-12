from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import colisiones
from django.db.models import Q
from .forms import ColisionesForm, ColisionesForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ColisionesListView(ListView):
    model = colisiones
    paginate_by = 50
    
@method_decorator(staff_member_required, name='dispatch')
class ColisionesDetailView(DetailView):
    model = colisiones

@method_decorator(staff_member_required, name='dispatch')
class ColisionesCreate(CreateView):
    model = colisiones
    form_class = ColisionesForm
    success_url = reverse_lazy('colisiones:colisiones')

@method_decorator(staff_member_required, name='dispatch')
class ColisionesUpdate(UpdateView):
    model = colisiones
    form_class = ColisionesForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('colisiones:updatecolisiones', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ColisionesDelete(DeleteView):
    model = colisiones
    success_url = reverse_lazy('colisiones:colisiones')

class FiltroColisionesListView(ListView):
    model = colisiones
    template_name= 'colisiones/colisiones_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return colisiones.objects.all()[:50]
        else:
            queryset =colisiones.objects.filter(Q(fecha__icontains=filter_val)| Q(nombre__icontains=filter_val)| Q(unidad__icontains=filter_val)
            | Q(patente__icontains=filter_val) 
            )
            
            return queryset[:50]
    
    
   