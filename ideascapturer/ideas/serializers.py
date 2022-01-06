from rest_framework.serializers import ModelSerializer, FileField, CharField
from .models import Idea


class IdeaSerializer(ModelSerializer):
    audio_file = FileField(required=False)
    idea_text = CharField(required=False)

    class Meta:
        model = Idea
        fields = ['id', 'idea_text', 'audio_file', 'created_at', 'updated_at']
