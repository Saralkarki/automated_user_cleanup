# Step 2 & 3: Define a custom User model by subclassing AbstractUser and add a custom field

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
	last_login = models.DateTimeField(default=timezone.now)
	is_active = models.BooleanField(default=True)
