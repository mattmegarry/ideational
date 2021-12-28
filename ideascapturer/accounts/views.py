from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import permissions


class Test(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return HttpResponse({"some": "data"})
