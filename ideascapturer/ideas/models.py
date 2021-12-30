from django.db import models
from django.conf import settings
from accounts.models import User


class Idea(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    idea_text = models.CharField(max_length=1000)
    audio_file = models.FileField(
        upload_to='ideas/audio/', blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.idea_text[0:50]
