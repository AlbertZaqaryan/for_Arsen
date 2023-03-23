from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('nout/<slug:slug>/', views.index_detail, name='index_detail'),
]