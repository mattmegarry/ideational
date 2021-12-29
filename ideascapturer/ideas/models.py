from django.db import models
from accounts.models import User


class Idea(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    idea_text = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.idea_text[0:50]
