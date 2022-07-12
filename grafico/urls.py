from django.urls import path
from .views import pie_chart
from . import views


urlpatterns = [
    path('pie-chart/', views.pie_chart, name='pie-chart'),
    
]