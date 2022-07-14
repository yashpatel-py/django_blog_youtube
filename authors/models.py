from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  # current user model

User = get_user_model()


class UserProfuile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=50, blank=True)
    dob = models.DateField(null=True, blank=True)
    profile_image = models.ImageField(upload_to="profile/", blank=True)
    website = models.URLField(blank=True)
    github = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
