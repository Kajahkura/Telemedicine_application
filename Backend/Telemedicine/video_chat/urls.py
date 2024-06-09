from django.urls import path
from .views import initiate_call, join_call, leave_call, room, video_conferencing

urlpatterns = [
    path('', video_conferencing, name='video_call'),
    path('initiate/', initiate_call, name='initiate_call'),
    path('join/<str:room_name>/', join_call, name='join_call'),
    path('leave/<str:room_name>/', leave_call, name='leave_call'),
    path('<str:room_name>/', room, name='room'),  # URL for rendering the room page
]
