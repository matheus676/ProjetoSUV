from .models import PostoDeSaude
from rest_framework import serializers

class PostoDeSaudeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostoDeSaude
        fields = '__all__'