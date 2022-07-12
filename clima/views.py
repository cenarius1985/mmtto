from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import clima
from django.db.models import Q
from .forms import ClimaForm, ClimaForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ClimaListView(ListView):
    model = clima
    paginate_by = 50

class ClimaDetailView(DetailView):
    model = clima

@method_decorator(staff_member_required, name='dispatch')
class ClimaCreate(CreateView):
    model = clima
    form_class = ClimaForm
    success_url = reverse_lazy('clima:clima')

@method_decorator(staff_member_required, name='dispatch')
class ClimaUpdate(UpdateView):
    model = clima
    form_class = ClimaForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('clima:updateclima', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ClimaDelete(DeleteView):
    model = clima
    success_url = reverse_lazy('clima:clima')

class FiltroClimaListView(ListView):
    model = clima
    template_name= 'clima/clima_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return clima.objects.all()[:50]
        else:
            queryset =clima.objects.filter(Q(servicio__icontains=filter_val)| Q(nombre__icontains=filter_val)
            | Q(marca__icontains=filter_val) | Q(modelo__icontains=filter_val)| Q(serie__icontains=filter_val)
            )
            
            return queryset[:50]