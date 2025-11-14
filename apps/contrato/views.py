from django.shortcuts import render
from .models import Contrato
from rest_framework import viewsets
from .serializer import ContratoSerializer

# Create your views here.

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer  