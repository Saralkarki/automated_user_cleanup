
from django.shortcuts import render

from .models import CleanupReport

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics

from .serializers import CleanupReportSerializer

def index(request):
	return render(request, 'index.html')

class CleanupReportLatest(generics.RetrieveAPIView):
	serializer_class = CleanupReportSerializer
	def get_object(self):
		try:
			return CleanupReport.objects.latest('timestamp')
		except CleanupReport.DoesNotExist:
			return Response(
				{'error': 'No cleanup reports found'}, 
				status=status.HTTP_404_NOT_FOUND
			)

class TriggerCleanup(APIView):
	def post(self, request):
		from .tasks import  log_inactive_users
		log_inactive_users.delay()
		
		return Response(
			{'message': 'Cleanup tasks triggered successfully'}, 
			status=status.HTTP_200_OK
		)
		



