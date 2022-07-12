from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import ordenes
from django.db.models import Q
from .forms import OrdenesForm, OrdenesForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class OrdenesListView(ListView):
    model = ordenes
    paginate_by = 50

class OrdenesDetailView(DetailView):
    model = ordenes

@method_decorator(staff_member_required, name='dispatch')
class OrdenesCreate(CreateView):
    model = ordenes
    form_class = OrdenesForm
    success_url = reverse_lazy('ordenes:ordenes')

@method_decorator(staff_member_required, name='dispatch')
class OrdenesUpdate(UpdateView):
    model = ordenes
    form_class = OrdenesForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ordenes:updateordenes', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class OrdenesDelete(DeleteView):
    model = ordenes
    success_url = reverse_lazy('ordenes:ordenes')

class FiltroOrdenesListView(ListView):
    model = ordenes
    template_name= 'ordenes/ordenes_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return ordenes.objects.all()[:50]
        else:
            queryset =ordenes.objects.filter(Q( serviciosolicita__icontains=filter_val)| Q(fecha__icontains=filter_val)| Q(detalle__icontains=filter_val)
            | Q(numerofolio__icontains=filter_val) | Q(estadoOT__icontains=filter_val)| Q(observaciones__icontains=filter_val)
            )
            
            return queryset[:50]
