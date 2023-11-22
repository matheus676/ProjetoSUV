from django.shortcuts import render
from .models import HistoricoDeVacinacao
from rest_framework import viewsets
from .serializer import HistoricoDeVacinacaoSerializer
# Create your views here.
class HistoricoDeVacinacaoViewSet(viewsets.ModelViewSet):
    queryset = HistoricoDeVacinacao.objects.all()
    serializer_class = HistoricoDeVacinacaoSerializer