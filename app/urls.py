from django.urls import path
from . import views

urlpatterns = [
    path('reports/latest/', views.CleanupReportLatest.as_view(), name='latest_report'),
    path('cleanup/trigger/', views.TriggerCleanup.as_view(), name='trigger_cleanup'),
]
