from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post
from django.core.mail import send_mail
from django.conf import settings
@receiver(post_save, sender=Post)
def send_notification_email(sender, instance, created, **kwargs):
    if created:
        print("Signal called on Post Created")
        subject = 'New Post Created'
        message = f'A new post titled "{instance.title}" has been created by {instance.author.username}.'
        from_email =   settings.EMAIL_HOST_USER # Replace with your email
        recipient_list = [instance.author.email]
        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            print("Exception: ",e)