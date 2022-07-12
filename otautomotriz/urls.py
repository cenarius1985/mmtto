from django.urls import path
from .views import OtautomotrizDelete, OtautomotrizCreate, OtautomotrizDetailView,OtautomotrizUpdate, OtautomotrizListView, FiltroOtautomotrizListView

otautomotriz_patterns = ([
    path('otautomotriz/', OtautomotrizListView.as_view(), name='otautomotriz'),
    path('otautomotriz/<int:pk>/', OtautomotrizDetailView.as_view(), name='detailotautomotriz'),
    path('create/otautomotriz', OtautomotrizCreate.as_view(), name='createotautomotriz'),
    path('otautomotriz/update/<int:pk>/', OtautomotrizUpdate.as_view(), name='updateotautomotriz'),
    path('otautomotriz/delete/<int:pk>/', OtautomotrizDelete.as_view(), name='deleteotautomotriz'),
    path('otautomotriz/filter/', FiltroOtautomotrizListView.as_view(), name='filtrootautomotriz'),
], 'otautomotriz')