from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Guia
from django.db.models import Q
from .forms import GuiaForm, GuiaForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class GuiaListView(ListView):
    model = Guia
    paginate_by = 50
    
class GuiaDetailView(DetailView):
    model = Guia

@method_decorator(staff_member_required, name='dispatch')
class GuiaCreate(CreateView):
    model = Guia
    form_class = GuiaForm
    success_url = reverse_lazy('guia:guia')

@method_decorator(staff_member_required, name='dispatch')
class GuiaUpdate(UpdateView):
    model = Guia
    form_class = GuiaForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('guia:updateguia', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class GuiaDelete(DeleteView):
    model = Guia
    success_url = reverse_lazy('guia:guia')

class FiltroGuiaListView(ListView):
    model = Guia
    template_name= 'informe/guia_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return Guia.objects.all()[:50]
        else:
            queryset =Guia.objects.filter(Q(nombre__icontains=filter_val)|Q(numero__icontains=filter_val))
            
            return queryset[:50]
    
    
   