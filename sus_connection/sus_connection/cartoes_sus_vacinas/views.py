from django.shortcuts import render
from .models import CartaoSus
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User



class CartaoCreate(CreateView):
    model = CartaoSus
    fields = ['cartaoSus']
    template_name = 'indexuplsus.html'
    success_url = reverse_lazy('sus-cadastrado')
    def form_valid(self, form):
        form.instance.users = self.request.user
        url = super().form_valid(form)
        return url



def ListarUsuarios(request):
    cartaoteste = CartaoSus.objects.all()
    
    for i in cartaoteste:
        if i.users.id == request.user.id:
            cartoes = CartaoSus.objects.get(users=request.user.id)
        else:
             cartoes = 'Você não cadastrou seu cartão do SUS por enquanto!'
    
    context = {
                'cartao': cartoes,
        }
    
    
    return render(request, "cartao_cadastrado.html", context)