from .models import MetodoPagamento
from rest_framework import viewsets
from .serializer import MetodoPagamentoSerializer
# Create your views here.

class MetodoPagamentoViewSet(viewsets.ModelViewSet):
    queryset = MetodoPagamento.objects.all()
    serializer_class = MetodoPagamentoSerializer 