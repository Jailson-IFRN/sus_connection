from django.shortcuts import render
from .models import Vacinas, Disponibilidade
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.decorators import login_required

class VacinasCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    group_required = "administrador"
    model = Vacinas
    fields = ['nome',"observacao","ubs"]
    template_name = 'form-excluir-vacinas.html'
    success_url = reverse_lazy('areaDoUsuario')


class VacinasUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    group_required = "funcionários"
    model = Vacinas
    fields = ['nome',"observacao","ubs"]
    template_name = 'form-editar-vacina.html'
    success_url = reverse_lazy('areaDoUsuario')

class VacinasDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    group_required = "administrador"
    model = Vacinas
    template_name = 'form-excluir-vacinas.html'
    success_url = reverse_lazy('areaDoUsuario')

class DisponibilidadeCreate(LoginRequiredMixin,GroupRequiredMixin, CreateView ):
    group_required = "funcionários"
    model = Disponibilidade
    fields = ['vacina',"disponibilidade","data"]
    template_name = 'form-cadastrar-vacinas.html'
    success_url = reverse_lazy('listar-vacinas')

@login_required(login_url='registrar')
def VacinasList(request):
        vacinas = Vacinas.objects.all()
        return render(request, 'lista-vacinas.html', {'vacinas': vacinas})

