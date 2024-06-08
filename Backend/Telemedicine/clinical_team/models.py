from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

class ClinicalTeamMember(models.Model):
    """
    Represents a member of the clinical team within the healthcare system.

    Attributes:
        member_id (CharField): Unique identifier for the team member (e.g., employee ID).
        first_name (CharField): Team member's first name.
        middle_name (CharField): Team member's middle name (optional).
        last_name (CharField): Team member's last name.
        role (CharField):  Team member's primary role (e.g., "Doctor", "Nurse", "Pharmacist", "Physiotherapist").
        specialization (CharField): Relevant specialization for doctors or other specialists (optional).
        phone_number (CharField): Team member's primary phone number (with validation).
        secondary_phone_number (CharField): An optional secondary phone number.
        email (EmailField): Team member's professional email address.
        license_number (CharField): Team member's professional license number (if applicable).
        license_state (CharField): State/region where the license was issued (if applicable).
        hospital_affiliation (CharField): Name of the hospital or clinic the team member is affiliated with.
        department (CharField): Department within the hospital where the team member works.
        office_location (CharField): Specific office or room number.
        office_hours (TextField): Team member's regular office hours (e.g., "Mon-Fri 9am-5pm").
        start_date (DateField): Date the team member started working at the current facility.
        profile_picture (ImageField): Image of the team member's profile picture (optional).
        biography (TextField): Short biography or introduction of the team member (optional).
        notes (TextField): Additional notes or information.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    member_id = models.CharField(max_length=20, unique=True, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50)

    role_choices = (
        ('DOC', 'Doctor'),
        ('NUR', 'Nurse'),
        ('PHA', 'Pharmacist'),
        ('PHY', 'Physiotherapist'),
        ('RAD', 'Radiographer'),
        # Add more roles as needed
    )
    role = models.CharField(max_length=3, choices=role_choices)

    specialization = models.CharField(max_length=100, blank=True, null=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be in E.164 format (e.g., +12125552368)")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, unique=True)
    secondary_phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True, null=True)
    email = models.EmailField()
    
    license_number = models.CharField(max_length=50, blank=True, null=True, unique=True)
    license_state = models.CharField(max_length=50, blank=True, null=True)
    hospital_affiliation = models.CharField(max_length=200)
    department = models.CharField(max_length=100)
    office_location = models.CharField(max_length=100)
    office_hours = models.TextField()

    start_date = models.DateField()
    profile_picture = models.ImageField(upload_to="team_member_profiles/", blank=True, null=True)
    biography = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.role == 'DOC':  # Special case for doctors
            return f"Dr. {self.first_name} {self.last_name} ({self.specialization})"
        else:
            return f"{self.first_name} {self.last_name} ({self.role})"
