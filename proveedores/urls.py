from django.urls import path
from .views import ProveedoresDelete, ProveedoresCreate, ProveedoresDetailView,ProveedoresUpdate, ProveedoresListView, FiltroProveedoresListView

proveedores_patterns = ([
    path('proveedores/', ProveedoresListView.as_view(), name='proveedores'),
    path('proveedores/<int:pk>/', ProveedoresDetailView.as_view(), name='detailproveedores'),
    path('create/proveedores', ProveedoresCreate.as_view(), name='createproveedores'),
    path('proveedores/update/<int:pk>/', ProveedoresUpdate.as_view(), name='updateproveedores'),
    path('proveedores/delete/<int:pk>/', ProveedoresDelete.as_view(), name='deleteproveedores'),
    path('proveedores/filter/', FiltroProveedoresListView.as_view(), name='filtroproveedores'),
], 'proveedores')