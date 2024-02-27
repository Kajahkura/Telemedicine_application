from django.urls import path
from . import views

#URL Routing
urlpatterns = [
        path('Health_Practitioneer/' , views.Health_practitioneer),
]
