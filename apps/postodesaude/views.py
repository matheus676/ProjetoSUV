from django.shortcuts import render
from .models import PostoDeSaude
from rest_framework import viewsets
from .serializer import PostoDeSaudeSerializer
# Create your views here.
class PostoDeSaudeViewSet(viewsets.ModelViewSet):
    queryset = PostoDeSaude.objects.all()
    serializer_class = PostoDeSaudeSerializer  
