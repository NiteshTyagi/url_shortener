from django.apps import AppConfig


class UrlShorteningConfig(AppConfig):
    name = 'url_shortening'

    def ready(self) -> None:
        from .signals import (url_post_save_signal)
