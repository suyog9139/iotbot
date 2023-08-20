from django.urls import path
from .views import CSVTemperatureUpload
from .views import LatestTemperature

urlpatterns = [
    path("upload-temperature/", CSVTemperatureUpload.as_view(), name='upload-temperature'),
    path("latest-temperature/", LatestTemperature.as_view(), name='latest-temperature'),
]
