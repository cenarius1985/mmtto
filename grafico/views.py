from django.shortcuts import render
from ropaexterno.models import ropaexterno
from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.db.models import Sum
import datetime

def pie_chart(request):
    labels = []
    data = []
    queryset = ropaexterno.objects.order_by('id')
    for ropa in queryset:
        labels.append(ropa.id)
        data.append(ropa.Valor)

    return render(request, 'grafico/pie_chart.html', {
        'labels': labels,
        'data': data,
    })

