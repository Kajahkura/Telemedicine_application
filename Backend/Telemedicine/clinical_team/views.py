from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import ClinicalTeamMember
from .forms import ClinicalTeamMemberRegistrationForm

def register_clinical_team_member(request):
    """
    View to handle clinical team member registration.

    Displays the registration form, processes the submitted data, validates it,
    creates a new user and ClinicalTeamMember object if valid, and redirects the
    user to the appropriate page.
    """
    if request.method == 'POST':
        form = ClinicalTeamMemberRegistrationForm(request.POST, request.FILES)  # Handle file uploads

        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, 'Staff member registered successfully!')
                # Redirect to a success page or the staff member's profile
                return redirect('staff_login')
            except Exception as e:  # Catch any unexpected errors
                messages.error(request, f'An error occurred during registration: {e}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ClinicalTeamMemberRegistrationForm()

    return render(request, 'clinical_team/register.html', {'form': form})

# Login views logic
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
