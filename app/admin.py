from django.contrib import admin
from .models import CleanupReport

# Register your models here.
# add the CleanupReport model to the admin dashboard
admin.site.register(CleanupReport)