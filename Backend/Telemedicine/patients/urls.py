from django.urls import path
from .views import patient_login_view, patient_logout_view, patient_home

urlpatterns = [
    path('patient/login', patient_login_view, name='patient_login'),
	path('patient/home', patient_home, name='patient_homepage'),
    path('patient/logout', patient_logout_view, name='patient_logout'),
]
