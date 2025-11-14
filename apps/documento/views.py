from django.shortcuts import render
from .models import Documento
from rest_framework import viewsets
from .serializer import DocumentoSerializer

# Create your views here.

class DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer 
