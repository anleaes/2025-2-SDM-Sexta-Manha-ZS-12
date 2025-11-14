from .models import ItemContrato
from rest_framework import serializers
    
class ItemContratoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemContrato
        fields = '__all__'