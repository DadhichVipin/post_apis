from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post

@receiver(post_save, sender=Post)
def send_notification_email(sender, instance, created, **kwargs):
    if created:
        print("Signal called on Post Created")