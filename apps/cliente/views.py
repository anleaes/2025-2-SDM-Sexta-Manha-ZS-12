from django.shortcuts import render
from .models import Cliente
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .serializer import ClienteSerializer

# Create your views here.
filter_backends = [DjangoFilterBackend]
filterset_fields = ['nome', 'numeroDocumento', 'telefone']

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer  
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'numeroDocumento', 'telefone']