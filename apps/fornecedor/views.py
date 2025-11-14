from django.shortcuts import render
from .models import Fornecedor
from rest_framework import viewsets
from .serializer import FornecedorSerializer
# Create your views here.
class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer 