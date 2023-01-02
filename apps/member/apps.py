from django.apps import AppConfig


class MemberConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    label = 'member'
    name = 'apps.member'
