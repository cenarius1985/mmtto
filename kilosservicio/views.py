from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import kilosservicio
from django.db.models import Q
from .forms import KilosservicioForm, KilosservicioForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class KilosservicioListView(ListView):
    model = kilosservicio
    paginate_by = 50

class KilosservicioDetailView(DetailView):
    model = kilosservicio

@method_decorator(staff_member_required, name='dispatch')
class KilosservicioCreate(CreateView):
    model = kilosservicio
    form_class = KilosservicioForm
    success_url = reverse_lazy('kilosservicio:kilosservicio')

@method_decorator(staff_member_required, name='dispatch')
class KilosservicioUpdate(UpdateView):
    model = kilosservicio
    form_class = KilosservicioForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('kilosservicio:updatekilosservicio', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class KilosservicioDelete(DeleteView):
    model = kilosservicio
    success_url = reverse_lazy('kilosservicio:kilosservicio')

class FiltroKilosservicioListView(ListView):
    model = kilosservicio
    template_name= 'kilosservicio/kilosservicio_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return kilosservicio.objects.all()[:50]
        else:
            queryset =kilosservicio.objects.filter(Q(Fecha__icontains=filter_val)| Q(serviciosolicita__icontains=filter_val)| Q(Cantidad__icontains=filter_val))
            
            return queryset[:50]


