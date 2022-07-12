from django.urls import path
from .views import RopaexternoDelete, RopaexternoCreate, RopaexternoDetailView,RopaexternoUpdate, RopaexternoListView, FiltroRopaexternoListView

ropaexterno_patterns = ([
    path('ropaexterno/', RopaexternoListView.as_view(), name='ropaexterno'),
    path('ropaexterno/<int:pk>/', RopaexternoDetailView.as_view(), name='detailropaexterno'),
    path('create/ropaexterno', RopaexternoCreate.as_view(), name='createropaexterno'),
    path('ropaexterno/update/<int:pk>/', RopaexternoUpdate.as_view(), name='updateropaexterno'),
    path('ropaexterno/delete/<int:pk>/', RopaexternoDelete.as_view(), name='deleteropaexterno'),
    path('ropaexterno/filter/', FiltroRopaexternoListView.as_view(), name='filtroropaexterno'),
], 'ropaexterno')