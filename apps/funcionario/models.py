from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField('nome', max_length=50)
    email = models.EmailField('email', max_length=50)
    senha = models.CharField('senha', max_length=15)
    cargo = models.CharField('cargo', default='efetivado', choices=['estagiario', 'jovem aprendiz', 'efetivado', 'Estagiario', 'Jovem aprendiz', 'Efetivado'])
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.client) 