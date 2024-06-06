from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Patient

def clinical_team_login_view(request):
    """
    Custom login view for clinical team members.

    Handles the login process for clinical staff, authenticating their credentials.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                request=request, 
                username=form.cleaned_data['username'], 
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'Welcome back!')
                return redirect('staff_homepage')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'clinical_team/login.html', {'form': form})

def clinical_team_homepage(request):
    if request.user.is_authenticated:
		return render(request, 'patients/dashboard.html')
	else:
		return redirect('clinical_team_login_view')

def clinical_team_logout_view(request):
    """
    Custom logout view for clinical team members.
    """
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('staff_login')  # Redirect to clinical team login page
