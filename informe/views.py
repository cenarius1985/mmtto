from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Informes
from django.db.models import Q
from .forms import InformesForm, InformesForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class InformesListView(ListView):
    model = Informes
    paginate_by = 50
    
class InformesDetailView(DetailView):
    model = Informes

@method_decorator(staff_member_required, name='dispatch')
class InformesCreate(CreateView):
    model = Informes
    form_class = InformesForm
    success_url = reverse_lazy('informes:informes')

@method_decorator(staff_member_required, name='dispatch')
class InformesUpdate(UpdateView):
    model = Informes
    form_class = InformesForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('informes:updateinformes', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class InformesDelete(DeleteView):
    model = Informes
    success_url = reverse_lazy('informes:informes')

class FiltroInformesListView(ListView):
    model = Informes
    template_name= 'informe/informes_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return Informes.objects.all()[:50]
        else:
            queryset =Informes.objects.filter(Q(nombre__icontains=filter_val)   )
            
            return queryset[:50]
    
    
   