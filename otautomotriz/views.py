from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import otautomotriz
from django.db.models import Q
from .forms import OtautomotrizForm, OtautomotrizForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class OtautomotrizListView(ListView):
    model = otautomotriz
    paginate_by = 50

class OtautomotrizDetailView(DetailView):
    model = otautomotriz

@method_decorator(staff_member_required, name='dispatch')
class OtautomotrizCreate(CreateView):
    model = otautomotriz
    form_class = OtautomotrizForm
    success_url = reverse_lazy('otautomotriz:otautomotriz')

@method_decorator(staff_member_required, name='dispatch')
class OtautomotrizUpdate(UpdateView):
    model = otautomotriz
    form_class = OtautomotrizForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('otautomotriz:updateotautomotriz', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class OtautomotrizDelete(DeleteView):
    model = otautomotriz
    success_url = reverse_lazy('otautomotriz:otautomotriz')

class FiltroOtautomotrizListView(ListView):
    model = otautomotriz
    template_name= 'otautomotriz/otautomotriz_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return otautomotriz.objects.all()[:50]
        else:
            queryset =otautomotriz.objects.filter(Q(fechaingreso__icontains=filter_val)| Q(numeroorden__icontains=filter_val)| Q(patente__icontains=filter_val)
            | Q(unidad__icontains=filter_val) | Q(tipo_mantenimiento__icontains=filter_val)| Q(observaciones__icontains=filter_val)
            )
            
            return queryset[:50]