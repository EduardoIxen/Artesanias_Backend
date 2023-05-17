from django.urls import path
from .views import index, login, logout, agregar_producto

urlpatterns = [
    path('index', index, name='index'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('agregarproducto', agregar_producto, name='agregar_producto'),
]