from django.apps import AppConfig
#settings.py 41번째 줄 추가

class PollsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "polls"
