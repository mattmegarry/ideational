from rest_framework.serializers import ModelSerializer, FileField
from .models import Idea


class IdeaSerializer(ModelSerializer):
    audio_file = FileField(required=False)

    class Meta:
        model = Idea
        fields = ['id', 'idea_text', 'audio_file', 'created_at', 'updated_at']
