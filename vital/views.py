from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from monitoreo.models import monitoreo
from monitoreo.forms import MonitoreoForm

class StaffRequiredMixin(object):
    """
    Este mixin requerirá que el usuario sea miembro del staff
    """
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

@method_decorator(staff_member_required, name='dispatch')
class VitalCreate(CreateView):
    model = monitoreo
    template_name = 'vital/vital_form.html'
    form_class = MonitoreoForm
    success_url = reverse_lazy('monitores:monitores')
    def form_valid(self, form):
        response= super().form_valid(form)
        form.instance.nombre='Monitor de Signos Vitales'
        form.instance.save()
        return response

class VitalDetailView(DetailView):
    model = monitoreo
    template_name = 'vital/vital_detail.html'

