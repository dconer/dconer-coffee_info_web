from django.apps import AppConfig


class ServicesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'services'  # the name by default
    verbose_name = 'Servicio'  # the name to overwrite
