# Generated by Django 5.2.3 on 2025-07-23 08:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, default='profile_images/default-avatar.png', upload_to='profile_images/')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(blank=True)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('languages', models.CharField(blank=True, max_length=255)),
                ('rating', models.FloatField(default=0.0)),
                ('sessions', models.IntegerField(default=0)),
                ('skills', models.IntegerField(default=0)),
                ('joined', models.DateField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
