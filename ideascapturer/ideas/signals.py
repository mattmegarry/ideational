from django.db.models.signals import post_save
from django.dispatch import receiver
from ideas.models import Idea
from ideas.utils import transcribe_audio


@receiver(post_save, sender=Idea)
def on_idea_created(sender, **kwargs):
    idea = kwargs['instance']
    if kwargs['created'] & bool(idea.audio_file):
        idea_id = idea.id
        saved_idea = Idea.objects.get(id=idea_id)
        transcribed_audio = transcribe_audio(saved_idea.audio_file)
        print(transcribed_audio)
