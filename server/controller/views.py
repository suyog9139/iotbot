from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import IoTData
import pandas as pd

class CSVTemperatureUpload(APIView):
    def post(self, request):
        data = request.data
        temperature = data.get('temperature')
        
        if temperature is not None:
            iot_data = IoTData.objects.create(temperature=temperature)
            return Response({"message": "Temperature data received and saved"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Temperature data not provided"}, status=status.HTTP_400_BAD_REQUEST)

class LatestTemperature(APIView):
    def get(self, request):
        try:
            latest_data = IoTData.objects.latest('timestamp')  # Get the latest data based on timestamp
            latest_temperature = latest_data.temperature
            return Response({"latest_temperature": latest_temperature}, status=status.HTTP_200_OK)
        except IoTData.DoesNotExist:
            return Response({"message": "No temperature data available"}, status=status.HTTP_404_NOT_FOUND)