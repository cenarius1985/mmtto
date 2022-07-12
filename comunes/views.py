from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import comunes
from django.db.models import Q
from .forms import ComunesForm, ComunesForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class ComunesListView(ListView):
    model = comunes
    paginate_by = 50

class ComunesDetailView(DetailView):
    model = comunes

@method_decorator(staff_member_required, name='dispatch')
class ComunesCreate(CreateView):
    model = comunes
    form_class = ComunesForm
    success_url = reverse_lazy('comunes:comunes')

@method_decorator(staff_member_required, name='dispatch')
class ComunesUpdate(UpdateView):
    model = comunes
    form_class = ComunesForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('comunes:updatecomunes', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class ComunesDelete(DeleteView):
    model = comunes
    success_url = reverse_lazy('comunes:comunes')

class FiltroComunesListView(ListView):
    model = comunes
    template_name= 'comunes/comunes_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return comunes.objects.all()[:50]
        else:
            queryset =comunes.objects.filter(Q(numerofactura__icontains=filter_val)| Q(fecha__icontains=filter_val)| Q(sector__icontains=filter_val)
            | Q(direccion__icontains=filter_val) | Q(numeromedidor__icontains=filter_val)| Q(numerocliente__icontains=filter_val)
            )
            
            return queryset[:50]