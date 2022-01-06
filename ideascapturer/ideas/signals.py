from django.db.models.signals import post_save
from django.dispatch import receiver
from ideas.models import Idea
from ideas.audio import transcribe_audio


@receiver(post_save, sender=Idea)
def on_idea_created(sender, **kwargs):
    if kwargs['created']:
        idea = kwargs['instance']
        if bool(idea.audio_file):
            transcribed_audio = transcribe_audio(idea.audio_file)
            idea.idea_text = transcribed_audio
            idea.save()
            print(transcribed_audio)
