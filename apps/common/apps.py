from django.apps import AppConfig


class CommonConfig(AppConfig):
    """Configuration for cross-cutting LiberFlow functionality."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.common"
    verbose_name = "Общее"
