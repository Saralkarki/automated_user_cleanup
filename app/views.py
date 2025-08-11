
from django.shortcuts import render
from .tasks import deactivate_inactive_users

def index(request):
	deactivate_inactive_users.delay()
	return render(request, 'index.html')

# Create your views here.
