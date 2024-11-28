from django.urls import path
from .views import CartaoCreate 
from . import views
urlpatterns = [
    path("cadastrar/cartao-do-sus", CartaoCreate.as_view() , name="cadastrar-sus"),
    path("cartao/cadastrado", views.ListarUsuarios , name="sus-cadastrado"),
]