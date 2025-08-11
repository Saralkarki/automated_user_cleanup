from django.utils import timezone
from datetime import timedelta
import os
from celery import shared_task
from django.contrib.auth import get_user_model
from .models import CleanupReport

@shared_task
def print_all_user_last_login():
    User = get_user_model()
    print("Printing all user last login times:")
    for user in User.objects.all():
        print(f"Username: {user.username}, Last login: {user.last_login}")

@shared_task
def deactivate_inactive_users():
    User = get_user_model()
    days = int(os.environ.get('INACTIVITY_THRESHOLD_DAYS', 30))
    threshold_date = timezone.now() - timedelta(days=days)

    # Bulk update all users whose last_login is older than threshold and are active
    User.objects.filter(is_active=True, last_login__lt=threshold_date).update(is_active=False)

# find inactive users and remove them from the db after logging
@shared_task
def log_inactive_users(batch_size=100):
    User = get_user_model()
    now = timezone.now()
    total_logged = 0

    while True:
        batch_user_ids = list(
            User.objects.filter(is_active=False)
                        .values_list('id', flat=True)[:batch_size]
        )
        if not batch_user_ids:
            break
        
        batch_count = len(batch_user_ids)
        User.objects.filter(id__in=batch_user_ids).delete()
        total_logged += batch_count

    # Create ONE CleanupReport entry at the end with total summary
    if total_logged > 0:
        active_users_count = User.objects.filter(is_active=True).count()
        CleanupReport.objects.create(
            timestamp=now,
            users_deleted=total_logged,
            active_users_remaining=active_users_count
        )

    return f"Logged and deleted {total_logged} inactive users"