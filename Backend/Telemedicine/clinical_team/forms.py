from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ClinicalTeamMember


class ClinicalTeamMemberRegistrationForm(UserCreationForm):
    """
    Form for registering new clinical team members.
    
    This form includes fields for collecting essential information about clinical 
    team members, including their user credentials and professional details.
    """
    confirm_email = forms.EmailField(label="Confirm Email", required=True)

    class Meta(UserCreationForm.Meta):
        model = ClinicalTeamMember
        fields = ['first_name', 'middle_name', 'last_name', 'role', 'specialization', 
                  'phone_number', 'secondary_phone_number', 'email',
                  'license_number', 'license_state', 'hospital_affiliation', 'department', 
                  'office_location', 'office_hours', 'start_date', 'profile_picture',
                  'biography', 'notes', 'member_id'] + UserCreationForm.Meta.fields

        # Add labels and widgets as before (unchanged from your previous code)
        # ...
    
    def clean(self):
        """Custom form-wide cleaning and validation."""
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email and email != confirm_email:
            self.add_error("confirm_email", "Email addresses do not match.")

        # Conditional validation for license based on role (customize as needed)
        role = cleaned_data.get("role")
        license_number = cleaned_data.get("license_number")
        license_state = cleaned_data.get("license_state")
        if role in ['DOC', 'NUR', 'PHA']:  # Doctors, Nurses, Pharmacists require license
            if not license_number:
                self.add_error("license_number", "License number is required for this role.")
            if not license_state:
                self.add_error("license_state", "License state is required for this role.")
        
        # Member ID uniqueness check
        member_id = cleaned_data.get("member_id")
        if ClinicalTeamMember.objects.filter(member_id=member_id).exists():
            self.add_error("member_id", "Staff ID already exists.")

        return cleaned_data

    def save(self, commit=True):
        """
        Overridden save method to set the patient_id for the associated Patient object.
        """
        user = super().save(commit=False)  # Create the user first
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()

        # Create and link the ClinicalTeamMember object
        member = ClinicalTeamMember.objects.create(
            user=user,
            **self.cleaned_data  # Pass cleaned data directly 
        )
        if commit:
            member.save()  
        return user
