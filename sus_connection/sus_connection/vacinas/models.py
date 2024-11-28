from django.db import models
from ubs.models import Ubs, DiaSemana


class Vacinas(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome da Vacina")
    observacao = models.CharField(max_length=400,verbose_name="Observação sobre a Vacina: ", blank=True, null=True, default=None)
    ubs = models.ManyToManyField(Ubs, verbose_name='Postos em que a vacina está disponível')
    def __str__(self) :
        return self.nome

class Disponibilidade(models.Model):
    vacina = models.ForeignKey(Vacinas,on_delete=models.CASCADE)
    disponibilidade = models.BooleanField(default=False, verbose_name='Está disponível?')
    data = models.ManyToManyField(DiaSemana, verbose_name='Em qual/quais dia(s), a vacina está disponível?', blank=True, null=True, default=None)
    data_atualizacao = models.DateTimeField( blank=True, null=True, default=None)
    def __str__(self):
        return self.vacina.nome
