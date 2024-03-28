# signals.py

from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Session


@receiver(post_save, sender=Session)
def calculate_session_score(sender, instance, created, **kwargs):
    """
    Signal to calculate session score after saving a Session instance.
    """
    if created:
        instance.calculate_score()
