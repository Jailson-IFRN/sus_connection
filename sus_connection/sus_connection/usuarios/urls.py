from django.urls import path
from django.contrib.auth import views as auth_views
from .views import DadosFuncCreate, registrar_duvida
from . import views 


urlpatterns = [
    #path("login/", views.loginn, name='login'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("cadastro-ou-login/", views.Usuarios, name='registrar'),
    path("areaDoUsuario/", views.Area_de_usuario, name='areaDoUsuario'),
    path("cadastrar/dados/complementares", DadosFuncCreate.as_view(), name='cadastro-complementar'),
    path("registrar/duvidas", views.registrar_duvida, name='registrar-duvidas'),
    path("registrar/respostas/<int:id>/", views.registrar_resposta, name='registrar-resposta'),
    path("listar/duvidas/", views.listar_todas_as_duvidas, name='listar-duvida'),
     path("ler/respostas/<int:id>/", views.listar_respostas, name='ler'),
    path('lermais/', views.lermais, name='lermais'),
]
