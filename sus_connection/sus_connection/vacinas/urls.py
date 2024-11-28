from django.urls import path
from .views import  VacinasUpdate,VacinasDelete, VacinasList, DisponibilidadeCreate
from . import views
urlpatterns = [
    path('cadastrar/disponibilidade/', DisponibilidadeCreate.as_view(), name='cadastrar-vacinas'),
    path('editar/vacinas/<int:pk>/', VacinasUpdate.as_view(), name='editar-vacinas'),
    path('excluir/vacinas/<int:pk>/', VacinasDelete.as_view(), name='excluir-vacinas'),
    path('listar/vacinas/', views.VacinasList, name='listar-vacinas'),
]