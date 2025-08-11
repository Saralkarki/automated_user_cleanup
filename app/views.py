from django.shortcuts import render
from automated_user_cleanup.celery import debug_task
from .tasks import print_all_user_last_login

def index(request):
	print_all_user_last_login.delay()
	return render(request, 'index.html')

# Create your views here.
