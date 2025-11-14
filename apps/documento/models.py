from django.db import models
from contrato.models import Contrato

# Create your models here.

class Documento(models.Model):
    nomeArquivo = models.CharField('nome Arquivo', max_length=50)
    tipoArquivo = models.CharField('tipo Arquivo', max_length=20, default='PDF', choices=[
        ('pdf', 'pdf'),
        ('jpeg', 'JPEG'),
        ('PNG', 'PNG'),])
    dataUpload = models.DateField('data Upload', max_length=10)
    contrato = models.ForeignKey(Contrato, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Arquivo'
        verbose_name_plural = 'Arquivos'
        ordering =['id']

    def __str__(self):
        return self.nomeArquivo