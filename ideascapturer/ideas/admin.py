from django.contrib import admin
from .models import Idea


class IdeaAdmin(admin.ModelAdmin):
    model = Idea


admin.site.register(Idea, IdeaAdmin)
