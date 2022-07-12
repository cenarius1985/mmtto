from django.urls import path
from .views import AnestesiaCreate, AnestesiaDetailView

anestesia_patterns = ([
    path('create_anestesia/', AnestesiaCreate.as_view(), name='create_anestesia'),
    path('<int:pk>/<slug:slug>/',AnestesiaDetailView.as_view(), name='anestesia'),
], 'anestesias')