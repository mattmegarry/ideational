from django.urls import path
from .views import (idea_view, picovoice_access_key_view)

urlpatterns = [
    path('', idea_view, name='ideas'),
    path('picovoice-key/', picovoice_access_key_view,
         name='picovoice_access_key'),
]
