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

from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from rest_framework.viewsets import GenericViewSet

class DataViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 data point
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many data points

      serializer_class = IotDataSerializer
      queryset = IotData.objects.all()
