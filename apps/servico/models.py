from django.db import models

# Create your models here.

class Servico(models.Model):
    nome = models.CharField('nome', max_length=50)
    descricao = models.CharField('descricao', max_length=50)
    precoBase = models.DecimalField('precoBase', max_digits=10, decimal_places=4)