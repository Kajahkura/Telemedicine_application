from django.urls import path
from .views import initiate_call, join_call, leave_call

urlpatterns = [
    path('initiate/', views.initiate_call, name='initiate_call'),
    path('join/<str:room_name>/', views.join_call, name='join_call'),
    path('leave/<str:room_name>/', views.leave_call, name='leave_call'),
]
