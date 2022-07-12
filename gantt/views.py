from django.views.generic.list import ListView
from monitoreo.models import monitoreo
from django.db.models import Q
import datetime

class FiltroEneroListView(ListView):
    model = monitoreo
    template_name= 'gantt/gantt_list.html'

    def get_queryset(self):
        ahora=str(datetime.date.today().year-1)
        filter_val = self.request.GET.get('buscar')
        if filter_val == "":
            return monitoreo.objects.filter(fecha__year=ahora, fecha__month='01')
        else:
            queryset =monitoreo.objects.filter(Q(fecha__year=ahora, fecha__month=filter_val))
            
            return queryset

class FiltroInicioListView(ListView):
    model = monitoreo
    template_name= 'gantt/gantt_list.html'
    def get_queryset(self):
        ahora=str(datetime.date.today().year-1)
        return monitoreo.objects.filter(fecha__year=ahora, fecha__month='01')

