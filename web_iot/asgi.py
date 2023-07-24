"""
ASGI config for web_iot project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from iot.consumers import IOTConsumerClass

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "web_iot.settings")

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter([
        path("iot", IOTConsumerClass.as_asgi())
    ])
})

