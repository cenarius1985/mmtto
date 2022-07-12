from django.urls import path
from .views import BasesDelete, BasesCreate, BasesDetailView,BasesUpdate, BasesListView, FiltroBasesListView

bases_patterns = ([
    path('bases/', BasesListView.as_view(), name='bases'),
    path('bases/<int:pk>/', BasesDetailView.as_view(), name='detailbases'),
    path('create/bases', BasesCreate.as_view(), name='createbases'),
    path('bases/update/<int:pk>/', BasesUpdate.as_view(), name='updatebases'),
    path('bases/delete/<int:pk>/', BasesDelete.as_view(), name='deletebases'),
    path('bases/filter/', FiltroBasesListView.as_view(), name='filtrobases'),
], 'bases')