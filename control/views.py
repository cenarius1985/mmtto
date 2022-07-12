from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import Control
from django.db.models import Q
from .forms import ControlForm, ControlForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ControlListView(ListView):
    model = Control
    paginate_by = 50
    
class ControlDetailView(DetailView):
    model = Control

@method_decorator(staff_member_required, name='dispatch')
class ControlCreate(CreateView):
    model = Control
    form_class = ControlForm
    success_url = reverse_lazy('Control:Control')

@method_decorator(staff_member_required, name='dispatch')
class ControlUpdate(UpdateView):
    model = Control
    form_class = ControlForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('Control:updateControl', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ControlDelete(DeleteView):
    model = Control
    success_url = reverse_lazy('Control:Control')

class FiltroControlListView(ListView):
    model = Control
    template_name= 'informe/Control_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return Control.objects.all()[:50]
        else:
            queryset =Control.objects.filter(Q(nombre__icontains=filter_val))
            
            return queryset[:50]
    
    
   