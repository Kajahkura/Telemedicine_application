# Generated by Django 5.0.2 on 2024-06-08 08:02

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinical_team', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='clinicalteammember',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clinicalteammember',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='clinicalteammember',
            name='license_number',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='clinicalteammember',
            name='phone_number',
            field=models.CharField(max_length=17, unique=True, validators=[django.core.validators.RegexValidator(message='Phone number must be in E.164 format (e.g., +12125552368)', regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
