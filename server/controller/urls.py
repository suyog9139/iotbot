from django.urls import path
from .views import CSVTemperatureUpload

urlpatterns = [
    path("upload-temperature/", CSVTemperatureUpload.as_view(), name='upload-temperature'),
]
