from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/video_chat/<str:room_name>/', consumers.VideoChatConsumer.as_asgi()),
]
