from .models import Vacina
from .models import LoteDeVacina
from rest_framework import serializers

class VacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vacina
        fields = '__all__'


class LoteDeVacinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoteDeVacina
        fields = '__all__'