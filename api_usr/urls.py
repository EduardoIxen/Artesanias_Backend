from django.urls import path
from .views import index, registro, login, get_productos, realizar_pedido, logout

urlpatterns = [
    path('index', index, name='index'),
    path('registro', registro, name='registro'),
    path('login', login, name='login'),
    path('productos', get_productos, name='productos'),
    path('pedido', realizar_pedido, name='pedido'),
    path('logout', logout, name='logout')
]