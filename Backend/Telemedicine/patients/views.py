from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # For displaying messages
from .models import Patient
from .forms import PatientRegistrationForm

def register_clinical_team_member(request):
    """
    View to handle Patients registration.

    Displays the registration form, processes the submitted data, validates it,
    creates a new user and patient object if valid, and redirects the
    user to the appropriate page.
    """
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST, request.FILES)  # Handle file uploads

        if form.is_valid():
            try:
                user = form.save()
                messages.success(request, 'Patient registered successfully!')
                # Redirect to a success page or the staff member's profile
                return redirect('patient_login')
            except Exception as e:  # Catch any unexpected errors
                messages.error(request, f'An error occurred during registration: {e}')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ClinicalTeamMemberRegistrationForm()

    return render(request, 'clinical_team/register.html', {'form': form})

# Patients login view
def patient_login_view(request):
    """
    Custom login view for patients.

    Handles the login process for patients, authenticating their credentials.
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
                return redirect('patient_homepage')
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'Templates/patient_login.html', {'form': form})

def patient_home(request):
        if request.user.is_authenticated:
            return render(request, 'patients/dashboard.html', context)
        else:
           # Redirect to login if user is not authenticated
            return redirect('patient_login')

def patient_logout_view(request):
    """Logs out the patient and redirects to the login page."""
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('patient_login')
