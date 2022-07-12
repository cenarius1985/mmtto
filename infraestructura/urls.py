from django.urls import path
from .views import InfraestructuraDelete, InfraestructuraCreate, InfraestructuraDetailView,InfraestructuraUpdate, InfraestructuraListView, FiltroInfraestructuraListView

infraestructura_patterns = ([
    path('infraestructura/', InfraestructuraListView.as_view(), name='infraestructura'),
    path('infraestructura/<int:pk>/', InfraestructuraDetailView.as_view(), name='detailinfraestructura'),
    path('create/infraestructura', InfraestructuraCreate.as_view(), name='createinfraestructura'),
    path('infraestructura/update/<int:pk>/', InfraestructuraUpdate.as_view(), name='updateinfraestructura'),
    path('infraestructura/delete/<int:pk>/', InfraestructuraDelete.as_view(), name='deleteinfraestructura'),
    path('infraestructura/filter/', FiltroInfraestructuraListView.as_view(), name='filtroinfraestructura'),
], 'infraestructura')