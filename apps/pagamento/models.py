from django.db import models
from contrato.models import Contrato
# Create your models here.

class Pagamento(models.Model):
    dataPagamento = models.DateField('Data', max_length=10)
    valorPago = models.DecimalField('valorPago', max_digits=10, decimal_places=2)
    metodoPagamento = models.CharField('metodoPagamento', max_length=20, default='cartao', choices=[
        ('boleto', 'Boleto'),
        ('cartao', 'Cartão de Crédito'),
        ('pix', 'PIX'),])
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'
        ordering =['id']

    def __str__(self):
        return "%s" % (self.cliente) 