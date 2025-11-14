from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome = models.CharField('nome', max_length=50)
    email = models.EmailField('email', max_length=50)
    senha = models.CharField('senha', max_length=15)
    CARGO_CHOICES = [
        ('estagiario', 'Estagiario'),
        ('jovemAprendiz', 'Jovem Aprendiz'),
        ('efetivado', 'Efetivado'),
    ]
    cargo = models.CharField('cargo', max_length=20, default='efetivado', choices=CARGO_CHOICES)
    
    class Meta:
        verbose_name = 'funcionario'
        verbose_name_plural = 'funcionarios'
        ordering =['id']

    def __str__(self):
        return self.nome