from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import hhee
from django.db.models import Q
from .forms import HHEEForm, HHEEForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class HHEEListView(ListView):
    model = hhee
    paginate_by = 50

class HHEEDetailView(DetailView):
    model = hhee

@method_decorator(staff_member_required, name='dispatch')
class HHEECreate(CreateView):
    model = hhee
    form_class = HHEEForm
    success_url = reverse_lazy('hhee:hhee')

@method_decorator(staff_member_required, name='dispatch')
class HHEEUpdate(UpdateView):
    model = hhee
    form_class = HHEEForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('hhee:updatehhee', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class HHEEDelete(DeleteView):
    model = hhee
    success_url = reverse_lazy('hhee:hhee')

class FiltroHHEEListView(ListView):
    model = hhee
    template_name= 'hhee/hhee_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return hhee.objects.all()[:50]
        else:
            queryset =hhee.objects.filter(Q( fecha__icontains=filter_val)| Q(nombre__icontains=filter_val)| Q(hhee__icontains=filter_val)
            | Q(motivo__icontains=filter_val)
            )
            
            return queryset[:50]

