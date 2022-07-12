from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Bases
from django.db.models import Q
from .forms import BasesForm, BasesForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class BasesListView(ListView):
    model = Bases
    paginate_by = 50
    
class BasesDetailView(DetailView):
    model = Bases

@method_decorator(staff_member_required, name='dispatch')
class BasesCreate(CreateView):
    model = Bases
    form_class = BasesForm
    success_url = reverse_lazy('bases:bases')

@method_decorator(staff_member_required, name='dispatch')
class BasesUpdate(UpdateView):
    model = Bases
    form_class = BasesForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('bases:updatebases', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class BasesDelete(DeleteView):
    model = Bases
    success_url = reverse_lazy('bases:bases')

class FiltroBasesListView(ListView):
    model = Bases
    template_name= 'informe/bases_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return Bases.objects.all()[:50]
        else:
            queryset =Bases.objects.filter(Q(nombre__icontains=filter_val)| Q(servicio__icontains=filter_val) )
            
            return queryset[:50]
    
    
   