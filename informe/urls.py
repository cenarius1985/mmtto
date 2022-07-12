from django.urls import path
from .views import InformesDelete, InformesCreate, InformesDetailView,InformesUpdate, InformesListView, FiltroInformesListView

informes_patterns = ([
    path('informes/', InformesListView.as_view(), name='informes'),
    path('informes/<int:pk>/', InformesDetailView.as_view(), name='detailinformes'),
    path('create/informes', InformesCreate.as_view(), name='createinformes'),
    path('informes/update/<int:pk>/', InformesUpdate.as_view(), name='updateinformes'),
    path('informes/delete/<int:pk>/', InformesDelete.as_view(), name='deleteinformes'),
    path('informes/filter/', FiltroInformesListView.as_view(), name='filtroinformes'),
], 'informes')