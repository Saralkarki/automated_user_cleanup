from django.db import models
from django.utils import timezone


# Model to log the results of each cleanup operation
class CleanupReport(models.Model):
	timestamp = models.DateTimeField(default=timezone.now)
	users_deleted = models.IntegerField()
	active_users_remaining = models.IntegerField()

	def __str__(self):
		return f"Cleanup at {self.timestamp}: {self.users_deleted} users deleted, {self.active_users_remaining} active users remaining"



