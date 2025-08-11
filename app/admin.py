
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from .models import CleanupReport


# Register your models here.
# add the CleanupReport model to the admin dashboard
class CleanupReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'users_deleted', 'active_users_remaining')
    ordering = ('-timestamp',)

admin.site.register(CleanupReport, CleanupReportAdmin)

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'date_joined','is_active','is_staff')
    # list_filter removed to hide filters
    search_fields = ('username', 'email', 'first_name', 'last_name')

# Unregister the default User admin
admin.site.unregister(User)
# Register the customized one
admin.site.register(User, CustomUserAdmin)
