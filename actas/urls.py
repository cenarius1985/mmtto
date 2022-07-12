from django.urls import path
from .views import ActasDelete, ActasCreate, ActasDetailView,ActasUpdate, ActasListView, FiltroActasListView

actas_patterns = ([
    path('actas/', ActasListView.as_view(), name='actas'),
    path('actas/<int:pk>/', ActasDetailView.as_view(), name='detailactas'),
    path('create/actas', ActasCreate.as_view(), name='createactas'),
    path('actas/update/<int:pk>/', ActasUpdate.as_view(), name='updateactas'),
    path('actas/delete/<int:pk>/', ActasDelete.as_view(), name='deleteactas'),
    path('actas/filter/', FiltroActasListView.as_view(), name='filtroactas'),
], 'actas')