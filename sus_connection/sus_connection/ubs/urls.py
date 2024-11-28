from django.urls import path
from .views import UbsCreate, IndexView, UbsUpdate, UbsDelete, UbsList, NoticiaCreate, NoticiasList, lerMais
from . import views 
urlpatterns = [
    path('cadastrar/ubs/', UbsCreate.as_view(), name='cadastrar-Ubs'),
    path('cadastrar/noticia/', NoticiaCreate.as_view(), name='cadastrar-noticia'),
    path('listar/noticias', NoticiasList.as_view(), name='listar-noticias'),
    path('', views.IndexView, name='inicio'),
    path('editar/ubs/<int:pk>/', UbsUpdate.as_view(), name='editar-Ubs'),
    path('excluir/ubs/<int:pk>/', UbsDelete.as_view(), name='excluir-Ubs'),
    path('listar/ubs/', UbsList.as_view(), name='listar-Ubs'),
    path("cadastrar/servico", views.CadastrarServico, name="cadastrar-servico"),
    path("detalhes/<int:id>/", views.detalhes, name="detalhes"),
    path("lermais/<int:id>/", views.lerMais, name="lermais"),
]
