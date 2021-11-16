from django.apps import AppConfig


class MnotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mnotes'

    def ready(self):
        import mnotes.signals