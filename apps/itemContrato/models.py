from django.db import models
from  contrato.models import Contrato
from servico.models import Servico

# Create your models here.

class ItemContrato(models.Model):
    quantidade = models.PositiveIntegerField('Quantidade',null=True, blank=True,default=0)
    valorUnitario = models.DecimalField('Preco unitario', max_digits=10, decimal_places=2)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)
    servico  = models.ForeignKey(Servico, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('contrato', 'servico')
        verbose_name = 'Item do contrato'
        verbose_name_plural = 'Itens do contrato'
        ordering =['id']

    def __str__(self):
        return f"{self.quantity} - {self.servico}"