from .models import Idea
from .serializers import IdeaSerializer
from rest_framework import mixins, generics, permissions


class IdeaList(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
