# chatapp/routing.py

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path, include
import chatapp.routing

application = ProtocolTypeRouter({
    "websocket": URLRouter(
        chatapp.routing.websocket_urlpatterns
    ),
})
