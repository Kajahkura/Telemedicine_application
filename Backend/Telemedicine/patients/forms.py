from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator, EmailValidator
from .models import Patient

class PatientRegistrationForm(forms.ModelForm):
    """
    Form for registering new patients.

    This form provides fields for collecting essential patient information,
    along with robust validation to ensure data integrity and accuracy.
    """

    # Additional field to confirm email address
    confirm_email = forms.EmailField(label="Confirm Email", required=True)

    class Meta:
        model = Patient
        fields = [
            'patient_id', 'first_name', 'middle_name', 'last_name',
            'date_of_birth', 'gender', 'phone_number', 'secondary_phone_number',
            'email', 'address', 'emergency_contact_name',
            'emergency_contact_phone', 'preferred_language', 'occupation',
            'marital_status', 'insurance_provider', 'insurance_policy_number',
            'insurance_group_number',
        ] + UserCreationForm.Meta.fields
        
        labels = {
            'patient_id': 'Patient ID (MRN)',
			'first_name': 'First Name',
            'middle_name': 'Middle Name',
            'last_name': 'Last Name',
            'date_of_birth': 'Date of Birth (YYYY-MM-DD)',
            'gender': 'Gender',
            'phone_number': 'Primary Phone Number',
            'secondary_phone_number': 'Secondary Phone Number (Optional)',
            'email': 'Email Address',
            'address': 'Residential Address',
            'emergency_contact_name': 'Emergency Contact Name',
            'emergency_contact_phone': 'Emergency Contact Phone Number',
            'preferred_language': 'Preferred Language',
            'occupation': 'Occupation',
            'marital_status': 'Marital Status',
            'insurance_provider': 'Insurance Provider',
            'insurance_policy_number': 'Insurance Policy Number',
            'insurance_group_number': 'Insurance Group Number',
            # ... add more labels as needed
        }
        
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
			'gender': forms.Select(attrs={'class': 'form-control'}),
			'marital_status': forms.Select(attrs={'class': 'form-control'}),
			'address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
        
    # Custom validation for email confirmation and patient ID uniqueness
    def clean(self):
        """
        Custom form-wide cleaning and validation.
        
        Checks for email confirmation match and patient ID uniqueness.
        """
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email and email != confirm_email:
            self.add_error("confirm_email", "Email addresses do not match.")

        patient_id = cleaned_data.get("patient_id")
        if Patient.objects.filter(patient_id=patient_id).exists():
            self.add_error("patient_id", "Patient ID already exists.")

        return cleaned_data


    def save(self, commit=True):
        """
        Overridden save method to set the patient_id for the associated Patient object.
        """
        # UserCreationForm will create the user and handle password hashing
        user = super().save(commit=False)  
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()

        # Create and link the Patient object
        patient = Patient.objects.create(
            user=user,
            **self.cleaned_data  # Pass cleaned data directly 
        )
        if commit:
            patient.save()  
        return user
