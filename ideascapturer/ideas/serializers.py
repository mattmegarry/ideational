from rest_framework import serializers
from .models import Idea


class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = ['id', 'idea_text', 'created_at', 'updated_at']
