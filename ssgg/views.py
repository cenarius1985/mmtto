from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from .models import cartola, moviles
from django.db.models import Q
from .forms import CartolaForm, CartolaForm2, MovilForm, MovilForm2


class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class CartolaListView(ListView):
    model = cartola
    paginate_by = 50

class CartolaDetailView(DetailView):
    model = cartola

@method_decorator(staff_member_required, name='dispatch')
class CartolaCreate(CreateView):
    model = cartola
    form_class = CartolaForm
    success_url = reverse_lazy('cartolas:cartolas')
    def form_valid(self, form):
        response= super().form_valid(form)
        kinicio= form.instance.kmi
        kfinal= form.instance.kmf
        form.instance.kmdt = kfinal-kinicio
        form.instance.save()
        return response

@method_decorator(staff_member_required, name='dispatch')
class CartolaUpdate(UpdateView):
    model = cartola
    form_class = CartolaForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('cartolas:updatecartola', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class CartolaDelete(DeleteView):
    model = cartola
    success_url = reverse_lazy('cartolas:cartolas')

class FiltroCartolaListView(ListView):
    model = cartola
    template_name= 'ssgg/cartola_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return cartola.objects.all()[:50]
        else:
            queryset =cartola.objects.filter(Q(patente__icontains=filter_val)| Q(fecha__icontains=filter_val)| Q(combustible__icontains=filter_val)
            | Q(uo__icontains=filter_val) | Q(pauta1__icontains=filter_val)
            )
            
            return queryset[:50]


############################Movilizacion################################

# Create your views here.
class MovilListView(ListView):
    model = moviles
    paginate_by = 50

class MovilDetailView(DetailView):
    model = moviles

@method_decorator(staff_member_required, name='dispatch')
class MovilCreate(CreateView):
    model = moviles
    form_class = MovilForm
    success_url = reverse_lazy('cartolas:moviles')

@method_decorator(staff_member_required, name='dispatch')
class MovilUpdate(UpdateView):
    model = moviles
    form_class = MovilForm2
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('cartolas:updatemovil', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class MovilDelete(DeleteView):
    model = moviles
    success_url = reverse_lazy('cartolas:moviles')

class FiltroMovilListView(ListView):
    model = moviles
    template_name= 'ssgg/movil_list.html'
    paginate_by = 50
    def get_queryset(self):
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return moviles.objects.all()[:50]
        else:
            queryset =moviles.objects.filter(Q(patente__icontains=filter_val)| Q(combustible__icontains=filter_val)
             | Q(servicio__icontains=filter_val)| Q(estado__icontains=filter_val)
            )
            
            return queryset[:50]