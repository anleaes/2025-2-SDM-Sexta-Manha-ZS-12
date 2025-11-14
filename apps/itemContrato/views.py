from django.shortcuts import render
from .models import ItemContrato
from rest_framework import viewsets
from .serializer import  ItemContratoSerializer
# Create your views here.
class ItemContratoViewSet(viewsets.ModelViewSet):
    queryset = ItemContrato.objects.all()
    serializer_class = ItemContratoSerializer  