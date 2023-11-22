from django.shortcuts import render
from .models import Vacina, LoteDeVacina
from rest_framework import viewsets
from .serializer import VacinaSerializer, LoteDeVacinaSerializer
# Create your views here.

class VacinaViewSet(viewsets.ModelViewSet):
    queryset = Vacina.objects.all()
    serializer_class = VacinaSerializer  

class LoteDeVacinaViewSet(viewsets.ModelViewSet):
    queryset = LoteDeVacina.objects.all()
    serializer_class = LoteDeVacinaSerializer