from django.apps import AppConfig

def ready(self):
    import blog.signals


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
