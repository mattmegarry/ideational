from django.apps import AppConfig


class IdeasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ideas'

    def ready(self):
        # Implicitly connect a signal handlers decorated with @receiver.
        from . import signals
