# api/views.py

from rest_framework import generics

from iot_data.models import IotData
from .serializers import IotDataSerializer


class IoTDataList(generics.ListAPIView):
    queryset = IotData.objects.all()
    serializer_class = IotDataSerializer


class IoTDataDetail(generics.RetrieveAPIView):
    queryset = IotData.objects.all()
    serializer_class = IotDataSerializer
