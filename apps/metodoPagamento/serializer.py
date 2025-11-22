from .models import MetodoPagamento
from rest_framework import serializers

class MetodoPagamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetodoPagamento
        fields = '__all__'