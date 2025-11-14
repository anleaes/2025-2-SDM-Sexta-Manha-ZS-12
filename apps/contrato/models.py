from django.db import models
from cliente.models import Cliente

# Create your models here.

class Contrato(models.Model):
    numeroContrato = models.CharField('Numero Contrato', max_length=50)
    dataInicio = models.DateField('Data', max_length=10)
    dataFim = models.DateField('Data', max_length=10)
    valorTotal = models.DecimalField('Valor Total', max_length=10)
    status = models.CharField('Status', max_length=20, default='andamento', choices=[
        ('andamento', 'Em andamento'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.client) 
from django.db import models
from cliente.models import Cliente

# Create your models here.


class Contrato(models.Model):
    numeroContrato = models.CharField('Numero Contrato', max_length=50)
    dataInicio = models.DateField('Data Inicio')
    dataFim = models.DateField('Data Fim')
    # DecimalField requires max_digits and decimal_places
    valorTotal = models.DecimalField('Valor Total', max_digits=12, decimal_places=2)
    status = models.CharField('Status', max_length=20, default='andamento', choices=[
        ('andamento', 'Em andamento'),
        ('finalizado', 'Finalizado'),
        ('cancelado', 'Cancelado'),
    ])
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        ordering = ['id']

    def __str__(self):
        # prefer showing the cliente's nome when possible
        if self.cliente and hasattr(self.numeroContrato, 'numero do contrato'):
            return self.cliente.nome
        return str(self.numeroContrato)
