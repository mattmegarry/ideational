from django.urls import path
from .views import (idea_view)

urlpatterns = [
    path('', idea_view, name='ideas'),
]
