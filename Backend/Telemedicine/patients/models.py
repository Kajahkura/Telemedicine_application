from django.db import models
from django.core.validators import RegexValidator

class Patient(models.Model):
    """
    Represents a patient within the healthcare system.

    Attributes:
        patient_id (CharField): Unique identifier for the patient.
        first_name (CharField): Patient's first name.
        middle_name (CharField): Patient's middle name (optional).
        last_name (CharField): Patient's last name.
        date_of_birth (DateField): Patient's date of birth.
        gender (CharField): Patient's gender (choices: 'M', 'F', 'O').
        phone_number (CharField): Patient's primary phone number (with validation).
        secondary_phone_number (CharField): An optional secondary phone number for the patient.
        email (EmailField): Patient's email address (optional).
        address (TextField): Patient's physical address.
        emergency_contact_name (CharField): Name of the patient's emergency contact person.
        emergency_contact_phone (CharField): Phone number of the emergency contact person.
        preferred_language (CharField): Patient's preferred language for communication.
        occupation (CharField): Patient's occupation (optional).
        marital_status (CharField): Patient's marital status (choices: 'S', 'M', 'D', 'W', 'O').
        insurance_provider (CharField): Name of the patient's insurance provider.
        insurance_policy_number (CharField): Patient's insurance policy number.
        insurance_group_number (CharField): Patient's insurance group number (optional).
        registration_date (DateField): Date the patient was registered in the system.
        notes (TextField): Additional notes or information about the patient (optional).
    """
    
    patient_id = models.CharField(max_length=20, unique=True, primary_key=True, help_text="Unique patient identifier (e.g., MRN)")
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True) 
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender_choices = (('M', 'Male'), ('F', 'Female'), ('O', 'Other'))
    gender = models.CharField(max_length=1, choices=gender_choices)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be in E.164 format (e.g., +12125552368)")
    phone_number = models.CharField(validators=[phone_regex], max_length=17)
    secondary_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    email = models.EmailField()
    address = models.TextField()

    emergency_contact_name = models.CharField(blank=True, null=True, max_length=100)
    emergency_contact_phone = models.CharField(validators=[phone_regex], blank=True, null=True,  max_length=17)

    preferred_language = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=100, blank=True, null=True)
    marital_status_choices = (('S', 'Single'), ('M', 'Married'), ('D', 'Divorced'), ('W', 'Widowed'), ('O', 'Other'))
    marital_status = models.CharField(max_length=1, choices=marital_status_choices, blank=True, null=True)

    insurance_provider = models.CharField(max_length=100, blank=True, null=True)
    insurance_policy_number = models.CharField(max_length=50, blank=True, null=True)
    insurance_group_number = models.CharField(max_length=50, blank=True, null=True)

    registration_date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, help_text="The date and time when the patient record was last updated.")
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.patient_id})"
