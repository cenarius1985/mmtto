from django.urls import path
from .views import DesfibriladorCreate, DesfibriladorDetailView

desfibrilador_patterns = ([
    path('create_desfibrilador/', DesfibriladorCreate.as_view(), name='create_desfibrilador'),
    path('<int:pk>/<slug:slug>/', DesfibriladorDetailView.as_view(), name='desfibrilador'),
], 'desfibriladores')