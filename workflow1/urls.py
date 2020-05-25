from django.urls import path
from . import views

urlpatterns = [
    path('invoke', views.index, name='index'),
]
