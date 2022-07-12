from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Prevencion
from django.db.models import Q
from .forms import PrevencionForm, PrevencionForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class PrevencionListView(ListView):
    model = Prevencion
    paginate_by = 50
    
class PrevencionDetailView(DetailView):
    model = Prevencion

@method_decorator(staff_member_required, name='dispatch')
class PrevencionCreate(CreateView):
    model = Prevencion
    form_class = PrevencionForm
    success_url = reverse_lazy('prevencion:prevencion')

@method_decorator(staff_member_required, name='dispatch')
class PrevencionUpdate(UpdateView):
    model = Prevencion
    form_class = PrevencionForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('prevencion:updateprevencion', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class PrevencionDelete(DeleteView):
    model = Prevencion
    success_url = reverse_lazy('prevencion:prevencion')

class FiltroPrevencionListView(ListView):
    model = Prevencion
    template_name= 'informe/prevencion_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return Prevencion.objects.all()[:50]
        else:
            queryset =Prevencion.objects.filter(Q(nombre__icontains=filter_val))
            
            return queryset[:50]
    
    
   