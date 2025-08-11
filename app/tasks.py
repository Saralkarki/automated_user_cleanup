from django.utils import timezone
from datetime import timedelta
import os
from celery import shared_task
from django.contrib.auth import get_user_model
# Step 1: Create a Celery task to print all user last login times

@shared_task
def print_all_user_last_login():
    User = get_user_model()
    print("Printing all user last login times:")
    for user in User.objects.all():
        print(f"Username: {user.username}, Last login: {user.last_login}")

@shared_task
def deactivate_inactive_users():
    User = get_user_model()
    now = timezone.now()
    # Get threshold from environment variable, default to 30 if not set
    days = int(os.environ.get('INACTIVITY_THRESHOLD_DAYS', 30))
    threshold = timedelta(days=days)
    for user in User.objects.all():
        if user.last_login and (now - user.last_login) > threshold:
            user.is_active = False
            user.save()
            print(f"Deactivated {user.username} (last login: {user.last_login})")