from django.urls import path
from .views import clinical_team_login_view, clinical_team_logout_view

urlpatterns = [
    path('login', clinical_team_login_view, name='staff_login'),
    path('logout', clinical_team_logout_view, name='staff_logout'),
	path('Professionals/home', clinical_team_homepage, name='staff_homepage')
]
