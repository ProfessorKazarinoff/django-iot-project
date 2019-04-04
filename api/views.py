# api/views.py

from rest_framework import generics

from iot_data.models import IotData
from .serializers import IotDataSerializer

from django.views.generic import DetailView

class IoTDataList(generics.ListAPIView):
    queryset = IotData.objects.all()
    serializer_class = IotDataSerializer

class IoTDataPointDetail(DetailView):
    model = IotData
    
    #queryset = IotData.objects.filter(channel_num=1)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
    #template_name = 'iotdata_list.html'
    template_name = 'onepoint.html'

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
