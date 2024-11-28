from django.db import models
from django.contrib.auth.models import User
from ubs.models import Ubs
from  django.utils import timezone

class DadosFunc(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cargo = models.CharField(max_length=50, verbose_name='Seu cargo: ', null=True)
    ubs = models.ForeignKey(Ubs, on_delete=models.CASCADE, verbose_name='UBS em que trabalha: ', null=True)
    foto = models.ImageField(upload_to='fotos_funcionarios', verbose_name='foto de perfil: ', null=True)

class Duvida(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    duvida = models.TextField(max_length=1000, null=True)
    imagem = models.ImageField(upload_to='fotos_respostas', null=True, blank=True)
    criadoin = models.DateTimeField(default=timezone.now)
    def __str__(self) :
        return self.duvida
    
class Respostas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    resposta = models.TextField(max_length=1000)
    duvida = models.ForeignKey(Duvida, null=True, on_delete=models.CASCADE)
    imagem = models.ImageField(upload_to='fotos_respostas', null=True, blank=True)
    criado = models.DateTimeField( default=timezone.now)
    def __str__(self) :
        return self.resposta

