from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import chat.routing

from chat.consumers import ChatConsumer
from django.urls import path

application = ProtocolTypeRouter({
    'websocket' : 
        URLRouter(
            path('ws/chat', ChatConsumer.as_asgi)
        )
})