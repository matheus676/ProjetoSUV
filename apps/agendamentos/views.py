from django.shortcuts import render
from .models import Agendamento
from rest_framework import viewsets
from .serializer import AgendamentoSerializer
# Create your views here.
class AgendamentoViewSet(viewsets.ModelViewSet):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer 

