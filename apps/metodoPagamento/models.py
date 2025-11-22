from django.db import models
from pagamento.models import Pagamento

# Create your models here.
class MetodoPagamento(models.Model):
    metodoPagamento = models.CharField('metodoPagamento', max_length=20, default='cartao', choices=[
        ('boleto', 'Boleto'),
        ('cartao', 'Cartão de Crédito'),
        ('pix', 'PIX'),
    ])

    pagamentos = models.ManyToManyField(Pagamento, related_name='metodos_pagamento')

    class Meta:
        verbose_name = 'Método de Pagamento'
        verbose_name_plural = 'Métodos de Pagamento'
        ordering = ['id']

    def __str__(self):
        return self.metodoPagamento