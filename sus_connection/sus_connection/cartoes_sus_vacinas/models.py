from django.db import models
from django.contrib.auth.models import User


class CartaoSus(models.Model):

    cartaoSus = models.ImageField(verbose_name='Cópia do Cartão do Sus ', upload_to="cartao_sus", null=True)
    
    users = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return self.cartaoSus.url