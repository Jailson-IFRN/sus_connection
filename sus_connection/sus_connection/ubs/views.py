from .models import Ubs, Noticias
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from .models import  Servicos
from vacinas.models import Vacinas
from django.shortcuts import render
from .forms import ServicosForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from usuarios.models import DadosFunc
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse
from datetime import datetime
from vacinas.models import Disponibilidade
from PIL import Image
import cv2
from datetime import datetime
from vacinas.models import Disponibilidade

def is_member_of_required_group(user):
    return user.groups.filter(name='funcionários').exists()


class UbsCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    group_required = "funcionários"
    model = Ubs
    fields = ['nome', 'bairro',"rua","numero","cep","referencia",'data_fundacao',  'horario_de_inicio','horario_de_termino', 'foto', 'cadastro_servico', 'dia']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-Ubs')
    


def detalhes(request, id):
    ubs = Ubs.objects.get(id=id)
    users_in_group = User.objects.all()
    dados = DadosFunc.objects.all()
    context = {
                'ubs': ubs,
                'usuarios': users_in_group, 
                'dados_func': dados, 
                'nome': ubs.nome
        }
    return render(request, "detalhes.html", context)

class UbsUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    group_required = "funcionários"
    model = Ubs
    fields = ['nome', 'bairro',"rua","numero","cep","referencia",'data_fundacao', 'horario_de_inicio', 'horario_de_termino', 'foto', 'cadastro_servico', 'dia']
    template_name = 'form.html'
    success_url = reverse_lazy('listar-Ubs')

class UbsDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = "funcionários"
    model = Ubs
    template_name = 'form-excluir.html'
    success_url = reverse_lazy('listar-Ubs')

class UbsList(ListView):
    model = Ubs
    template_name = 'listas.html'
    paginate_by = 2
    def get_queryset(self):
        nome = self.request.GET.get("nome")
        if nome:
            ubss = Ubs.objects.filter(nome__icontains = nome)
        else:
            ubss = Ubs.objects.all()
        return ubss

    
class NoticiasList(ListView):
    model = Noticias
    template_name = 'listar_noticias.html'
    paginate_by = 1
    def get_queryset(self):
        titulo = self.request.GET.get("nome")
        if titulo:
            noticias = Noticias.objects.filter(nome__icontains = titulo)
        else:
            noticias = Noticias.objects.all()
        return noticias
    

def lerMais(request, id):
    noticia = Noticias.objects.get(id=id)
    context = {
                'noticia': noticia,
        }
    return render(request, "lermais.html", context)



class NoticiaCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    group_required = "funcionários"
    model = Noticias
    fields = ['titulo', 'body',"imagem","ubs_relacionada", "data", "destaque"]
    template_name = 'cadastrar_noticia.html'
    success_url = reverse_lazy('areaDoUsuario')
    def form_valid(self, form):
        # Define o usuário como usuário logado
        contador = 0
        noticias = Noticias.objects.all()
        for i in noticias:
            if i.destaque == True:
                contador += 1
                if contador > 4:
                    group_required = "funcionários"
                    model = Noticias
                    fields = ['titulo', 'body',"imagem","ubs_relacionada", "data", "destaque"]
                    template_name = 'cadastrar_noticia.html'
                    success_url = reverse_lazy('areaDoUsuario')
                    return HttpResponse("Existe um limite de 5 noticías de destaque. Desmarque uma para cadastrar uma nova. ")
                else:
                    group_required = "funcionários"
                    model = Noticias
                    fields = ['titulo', 'body',"imagem","ubs_relacionada", "data", "destaque"]
                    template_name = 'cadastrar_noticia.html'
                    success_url = reverse_lazy('areaDoUsuario')
        
        form.instance.usuario = self.request.user
        url = super().form_valid(form)
        return url








def IndexView(request):
    if request.method == 'GET':
        ubss = Ubs.objects.all()
        servicoss = Servicos.objects.all()
        noticias2 = Noticias.objects.all()
        context = {
                'UBS': ubss,
                'Servicos': servicoss,
                'noticias': noticias2,
                'imagens': list
        }
    return render(request, "index.html", context)

@login_required(login_url='login')
@user_passes_test(is_member_of_required_group, login_url='registrar')
def CadastrarServico(request):
    if request.method == 'GET':
        servicos = Servicos.objects.all()
        return render(request, 'cadastrar_servico.html', {'servicos': servicos})
    elif request.method == 'POST':
        servico = request.POST.get('servicos')
        sv= Servicos(servico=servico)
        sv.save()
        servicos = Servicos.objects.all()
        return render(request, 'cadastrar_servico.html', {'servicos': servicos})
    
