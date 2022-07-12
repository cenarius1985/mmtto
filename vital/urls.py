from django.urls import path
from .views import VitalCreate, VitalDetailView

vital_patterns = ([
    path('create_vital/', VitalCreate.as_view(), name='create_vital'),
    path('<int:pk>/<slug:slug>/', VitalDetailView.as_view(), name='vital'),
], 'vitales')