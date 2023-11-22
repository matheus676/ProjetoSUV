from .models import HistoricoDeVacinacao
from rest_framework import serializers

class HistoricoDeVacinacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricoDeVacinacao
        fields = '__all__'