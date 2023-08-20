from django.urls import path
from .views import CSVTemperatureUpload
# from .views import TemperatureDataList
from .views import TemperatureDataList
urlpatterns = [
    path("upload-temperature/", CSVTemperatureUpload.as_view(), name='upload-temperature'),
    path('temperature-data/', TemperatureDataList.as_view(), name='temperature-data'),
]
