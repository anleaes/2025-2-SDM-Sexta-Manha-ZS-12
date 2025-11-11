from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=50)
    numeroDocumento = models.CharField('CPF/CNPJ', max_length=14)
    telefone = models.CharField('Telefone celular', max_length=20)
    email = models.EmailField('E-mail',null=False, blank=False)
    endereco = models.CharField('Endereco', max_length=200)   

    
    class Meta:
            verbose_name = 'Cliente'
            verbose_name_plural = 'Clientes'
            ordering =['id']

    def __str__(self):
        return self.first_name