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
