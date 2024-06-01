# Generated by Django 5.0.2 on 2024-06-01 10:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalTeamMember',
            fields=[
                ('member_id', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('DOC', 'Doctor'), ('NUR', 'Nurse'), ('PHA', 'Pharmacist'), ('PHY', 'Physiotherapist'), ('RAD', 'Radiographer')], max_length=3)),
                ('specialization', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='Phone number must be in E.164 format (e.g., +12125552368)', regex='^\\+?1?\\d{9,15}$')])),
                ('secondary_phone_number', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be in E.164 format (e.g., +12125552368)', regex='^\\+?1?\\d{9,15}$')])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('license_number', models.CharField(blank=True, max_length=50, null=True)),
                ('license_state', models.CharField(blank=True, max_length=50, null=True)),
                ('hospital_affiliation', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=100)),
                ('office_location', models.CharField(max_length=100)),
                ('office_hours', models.TextField()),
                ('start_date', models.DateField()),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='team_member_profiles/')),
                ('biography', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]