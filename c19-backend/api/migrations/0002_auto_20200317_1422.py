# Generated by Django 3.0.4 on 2020-03-17 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='C19APIPatientProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_nhs_number', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='c19_api_user_profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Covid-19 API User Profile',
                'verbose_name_plural': 'Covid-19 API User Profiles',
            },
        ),
        migrations.DeleteModel(
            name='C19APIUserProfile',
        ),
    ]
