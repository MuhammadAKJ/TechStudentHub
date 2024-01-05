from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    skills = models.CharField(max_length=255, blank=True)
    interests = models.CharField(max_length=255, blank=True)
    portfolio_url = models.URLField(blank=True)
    contact_email = models.EmailField(blank=True)
    phone_number = models.PhoneNumberField(blank=True)
    public_profile = models.BooleanField(default=True)
    # social media links
    twitter_url = models.CharField(max_length=255, blank=True)
    linkedin_url = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
