from django.urls import path
from . import views

urlpatterns = [
    path('', views.IdeaList.as_view(), name='ideas_list'),
]
