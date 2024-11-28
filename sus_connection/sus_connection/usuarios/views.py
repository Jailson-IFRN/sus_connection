from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from ubs.models import Ubs, Noticias
from .models import DadosFunc, Respostas, Duvida
from django.views.generic.edit import CreateView
from braces.views import GroupRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test


def is_member_of_required_group(user):
    return user.groups.filter(name='funcionários').exists()

def lermais(request):
    return render(request, 'lermais.html')

def Usuarios(request):
    if request.method == 'GET':
        return render(request, 'loginEcadastro.html')
    
    else:
        if 'cadastro' in request.POST:
            if request.POST.get('senha') == request.POST.get('confirmasenha'):
                try:
                    user = User.objects.create_user(username=request.POST.get('nome'), email = request.POST.get('email'), password=request.POST.get('senha'))
                    user.save()
                    login(request, user)
                    return render (request,'pagina_de_usuario.html')
                except:
                    context = {
                        'form': UserCreationForm,
                        'error': 'Usuário já existe'
                    }
                    return render(request, 'loginEcadastro.html', context)
        else:
            user = authenticate(
            request, username = request.POST.get("username"), password = request.POST.get("senhaUser"))

            if user is None:
                context={
                    'form': AuthenticationForm,
                    'error1': "Usuário ou senha estão incorretos"
                }
                return render(request, 'loginEcadastro.html', context)
            else:
                login(request, user)
                return redirect('areaDoUsuario')

class DadosFuncCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    group_required = "funcionários"
    model = DadosFunc
    fields = ['cargo', 'ubs',"foto"]
    template_name = 'meus_dados.html'
    success_url = reverse_lazy('areaDoUsuario')
    def form_valid(self, form):
        # Define o usuário como usuário logado
        form.instance.user = self.request.user
        url = super().form_valid(form)
        return url

@login_required(login_url='registrar')
def Area_de_usuario(request):
    if request.method == 'GET':
        ubss = Ubs.objects.all()
        noticias = Noticias.objects.all()
        dados = DadosFunc.objects.all()
        users = User.objects.filter(groups__name='funcionários')
        users2 = User.objects.all()
        context = {
                'UBS': ubss,
                'Noticias': noticias, 
                'Users_date': dados, 
                'usuarios': users,
                'usuarios2': users2
        }
    return render(request, "pagina_de_usuario.html", context)


@login_required(login_url='registrar')
def registrar_duvida(request):
    if request.method == "GET":
        user = request.user
        object_list = Duvida.objects.filter(user = user)
        context = {
                'duvidas': object_list,
        }
        return render (request, "registrar_duvida.html",  context)
    else:
        user = request.user
        duvida = request.POST.get('message')
        imagem = request.POST.get('foto_imagem')
        obj = Duvida(user=user, duvida= duvida, imagem = imagem )
        obj.save()
        return render(request, 'pagina_de_usuario.html')

@login_required(login_url='registrar')
@user_passes_test(is_member_of_required_group, login_url='registrar')
def registrar_resposta(request, id):
    duv = Duvida.objects.get(id=id)
    if request.method == "POST":
        duv = Duvida.objects.get(id=id)
        user = request.user
        resposta = request.POST.get('resposta')
        imagem = request.POST.get('foto_imagem')
        obj = Respostas(user=user, resposta= resposta, duvida=duv, imagem = imagem )
        obj.save()
        return render(request, 'pagina_de_usuario.html', {'duv': duv})
    else:
        duvida = Duvida.objects.get(id=id)
        respostas = Respostas.objects.filter(duvida=duvida)
        context = {
                'resposta': respostas,
                'duvida': duvida,
        }
        return render(request, 'registrar_resposta.html', context)

@login_required(login_url='registrar')
@user_passes_test(is_member_of_required_group, login_url='registrar')
def listar_todas_as_duvidas(request):
    duvidas = Duvida.objects.all()    
    return render(request, 'listarDuvidas.html', {'duv': duvidas}) 


@login_required(login_url='registrar')
def listar_respostas(request, id):
    if request.method == 'GET':
        duvida = Duvida.objects.get(id=id)
        respostas = Respostas.objects.filter(duvida=duvida)
        if not respostas:
            mensagem = 'Sem respostas por enquanto!'
        else:
            mensagem = ''
        context = {
                'resposta': respostas,
                'duvida': duvida,
                'mensagem': mensagem
        }
        return render(request, 'lerrespostas.html', context)
    else:
        duv = Duvida.objects.get(id=id)
        user = request.user
        resposta = request.POST.get('mensagem')
        imagem = request.POST.get('foto')
        obj = Respostas(user=user, resposta= resposta, duvida=duv, imagem = imagem )
        obj.save()
        duvida = Duvida.objects.get(id=id)
        respostas = Respostas.objects.filter(duvida=duvida)
        if not respostas:
            mensagem = 'Sem respostas por enquanto!'
        else:
            mensagem = ''
        context = {
                'resposta': respostas,
                'duvida': duvida,
                'mensagem': mensagem,
        }
        return render(request, 'lerrespostas.html', context)


