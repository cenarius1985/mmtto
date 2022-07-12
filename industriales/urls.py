from django.urls import path
from .views import IndustrialesDelete, IndustrialesCreate, IndustrialesDetailView,IndustrialesUpdate, IndustrialesListView, FiltroIndustrialesListView

industriales_patterns = ([
    path('industriales/', IndustrialesListView.as_view(), name='industriales'),
    path('industriales/<int:pk>/', IndustrialesDetailView.as_view(), name='detailindustriales'),
    path('create/industriales', IndustrialesCreate.as_view(), name='createindustriales'),
    path('industriales/update/<int:pk>/', IndustrialesUpdate.as_view(), name='updateindustriales'),
    path('industriales/delete/<int:pk>/', IndustrialesDelete.as_view(), name='deleteindustriales'),
    path('industriales/filter/', FiltroIndustrialesListView.as_view(), name='filtroindustriales'),
], 'industriales')