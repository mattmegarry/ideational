from .models import Idea
from .serializers import IdeaSerializer
from rest_framework import mixins, generics, permissions


class IdeaView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        print(request.data)
        audio_file_uploaded = request.FILES.get('audio_file')
        if audio_file_uploaded:
            content_type = audio_file_uploaded.content_type
            print(audio_file_uploaded)
            print(content_type)
        return self.create(request, *args, **kwargs)


idea_view = IdeaView.as_view()
