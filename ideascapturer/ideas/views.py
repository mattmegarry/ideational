from .models import Idea
from .serializers import IdeaSerializer
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser


class IdeaView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer
    parser_classes = [MultiPartParser, FormParser]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        audio_file_uploaded = request.FILES.get('audio_file')
        if audio_file_uploaded:
            content_type = audio_file_uploaded.content_type
            print(audio_file_uploaded)
            print(content_type)
        return self.create(request, *args, **kwargs)


idea_view = IdeaView.as_view()


class PicovoiceAccessKeyView(APIView):
    # Authentication, but not authorization, is handled in settings.py
    def get(self, request):
        # Hardcoded key - don't do this
        return Response({'accessKey': 'tNxjWgo/Wn6CRltFkIQOfUUE0Tl9HCBZ7vsAYQFt5vqO57yKAjL2wQ=='})


picovoice_access_key_view = PicovoiceAccessKeyView.as_view()
