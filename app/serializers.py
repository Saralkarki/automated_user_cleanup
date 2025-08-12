from rest_framework import serializers
from .models import CleanupReport


class CleanupReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleanupReport
        fields = ['id', 'timestamp', 'users_deleted', 'active_users_remaining']
        read_only_fields = ['id', 'timestamp', 'users_deleted', 'active_users_remaining']
