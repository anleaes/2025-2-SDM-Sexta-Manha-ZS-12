from django.db import models

# Create your models here.

class Fornecedor(models.Model):
    nome = models.CharField('nome fornecedor', max_length=50)
    cnpj = models.CharField('CNPJ', max_length=14)
    telefone = models.CharField('telefone', max_length=9)
    email = models.CharField('email', max_length=50)
    endereco = models.CharField('endereco', max_length=50)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.nome)