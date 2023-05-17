from django.urls import path
from .views import index, registro

urlpatterns = [
    path('index', index, name='index'),
    path('registro', registro, name='registro'),
]