import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'automated_user_cleanup.settings')

app = Celery('automated_user_cleanup')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')


app.autodiscover_tasks()

# # Schedule deactivate_inactive_users to run every 5 minutes
# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     sender.add_periodic_task(300.0, deactivate_inactive_users.s(), name='Deactivate inactive users every 5 min')


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print('*** CELERY DEBUG TASK EXECUTED ***')
    # print(f'Request: {self.request!r}')
    print("------------")