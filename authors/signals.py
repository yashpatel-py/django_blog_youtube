from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from .models import UserProfuile

user = get_user_model()


@receiver(post_save, sender=user)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfuile.objects.create(user=instance)
