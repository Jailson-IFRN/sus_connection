from django.db import models
from django.contrib.auth.models import User



class Servicos(models.Model):
    servico = models.CharField(max_length=500, verbose_name='Serviço: ')
    descricao = models.CharField(max_length=500, verbose_name='Descrição do serviço: ')
    def __str__(self) :
        return self.servico


class DiaSemana(models.Model):
    dia = models.CharField(max_length=20, verbose_name='Dias da semana de atendimento')

    def __str__(self):
        return self.dia
  
    
class Bairro(models.Model):
    bairro = models.CharField(max_length=50)
    def __str__(self):
        return self.bairro

class Ubs(models.Model):
    nome = models.CharField(max_length=250, verbose_name='Nome: ')
    bairro = models.ForeignKey(Bairro, verbose_name="Bairro: ", on_delete=models.CASCADE)
    rua = models.CharField(max_length=150, verbose_name="Rua: ")
    numero = models.PositiveIntegerField(verbose_name="Número: ")
    cep = models.CharField(max_length=10, verbose_name="Cep: ")
    referencia = models.CharField(max_length=120, verbose_name="Ponto de Referência: ")
    data_fundacao = models.DateField(verbose_name='Data de fundação: ')
    foto = models.ImageField(verbose_name='Imagem da UBS: ', upload_to="fotos_ubs")
    horario_de_inicio = models.TimeField( verbose_name='Horário de início de atendimento' )
    horario_de_termino = models.TimeField( verbose_name='Horário de término de atendimento' )
    cadastro_servico = models.ManyToManyField(Servicos)
    dia = models.ManyToManyField(DiaSemana, verbose_name='Dias de funcionamento: ')
    def __str__(self) :
        return self.nome
    

class Noticias(models.Model):
    titulo = models.CharField(max_length=200, verbose_name='Título da notícia')
    body = models.TextField(max_length=1000, verbose_name='Notícia')
    imagem = models.ImageField(verbose_name='Foto ilustrativa da notícia', upload_to='fotos_noticias')
    ubs_relacionada = models.ManyToManyField(Ubs, verbose_name='UBSs que a notícia se relaciona: ')
    data = models.DateTimeField(verbose_name='Data da notícia ou do Informe: ', null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    destaque = models.BooleanField(default=False, verbose_name="Notícia de destaque?")
    def __str__(self) :
        return self.titulo
    
from django import forms
from .models import DiaSemana

class DiaSemanaForm(forms.ModelForm):
    class Meta:
        model = DiaSemana
        fields = ['dia']

    def __init__(self, *args, **kwargs):
        super(DiaSemanaForm, self).__init__(*args, **kwargs)
        self.fields['dia'].widget = forms.CheckboxSelectMultiple()
