from django.urls import path
from .views import CartolaCreate, CartolaDelete, CartolaDetailView, CartolaListView, CartolaUpdate, CreateView, FiltroCartolaListView, MovilCreate, MovilDelete, MovilDetailView, MovilListView, MovilUpdate, FiltroMovilListView

cartolas_patterns = ([
    path('cartolas/', CartolaListView.as_view(), name='cartolas'),
    path('cartola/<int:pk>/', CartolaDetailView.as_view(), name='cartola'),
    path('create/cartola', CartolaCreate.as_view(), name='createcartola'),
    path('cartola/update/<int:pk>/', CartolaUpdate.as_view(), name='updatecartola'),
    path('cartola/delete/<int:pk>/', CartolaDelete.as_view(), name='deletecartola'),
    path('cartola/filter/', FiltroCartolaListView.as_view(), name='filtrocartola'),

    path('moviles/', MovilListView.as_view(), name='moviles'),
    path('moviles/<int:pk>/', MovilDetailView.as_view(), name='movil'),
    path('create/moviles', MovilCreate.as_view(), name='createmovil'),
    path('moviles/update/<int:pk>/', MovilUpdate.as_view(), name='updatemovil'),
    path('moviles/delete/<int:pk>/', MovilDelete.as_view(), name='deletemovil'),
    path('moviles/filter/', FiltroMovilListView.as_view(), name='filtromovil'),
], 'cartolas')