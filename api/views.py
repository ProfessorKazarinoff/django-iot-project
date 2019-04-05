# api/views.py

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.generics import RetrieveAPIView
from iot_data.models import IotData
from .serializers import IotDataSerializer

from django.views.generic import DetailView
from django.http import HttpResponse, JsonResponse


def create_db_entry(request, api_key_str, channel_pk, field_pk, data_str):
    """
    function-based view to write a data point to the database
    """
    if api_key_str == 'ABC':
        entry=IotData.objects.create(channel_num=int(channel_pk),field_num=int(field_pk), data=float(data_str), uploaded_by='peter')
        #return HttpResponse('<h1>Success</h1>')
        response_dict = {
            "channel": channel_pk,
            "field": field_pk,
            "data": data_str
        }
        return JsonResponse(response_dict)

    else:
        return HttpResponse('<h1>invalid api key</h1>')

class LatestDataView(RetrieveAPIView):
    queryset = IotData.objects.all()
    # add your serializer
    serializer_class = IotDataSerializer

    def get_object(self, *args, **kwargs):
        return self.queryset.filter(channel_num=kwargs.get('channel_pk')).latest('created_at')
        objects.latest('pub_date')

# def latest_data_point_view(request, channel_pk):
#     #latest_entry = IotData.objects.latest('created_at')
#     result = IotData.objects.all()
#     response_dict = dict(result)
#     #queryset = IotData.objects.all()
#     #latest_entry = queryset.objects.latest('created_at')
#     # add your serializer
#     #serializer_class = IotDataSerializer
#     return JsonResponse(response_dict, safe=False)

class IoTDataList(generics.ListAPIView):
    queryset = IotData.objects.all()
    serializer_class = IotDataSerializer


class IoTDataPointDetail(DetailView):
    model = IotData
    template_name = 'onepoint.html'


class IoTDataDetail(generics.RetrieveAPIView):
    queryset = IotData.objects.all()
    serializer_class = IotDataSerializer


class DataViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 data point
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many data points

      serializer_class = IotDataSerializer
      queryset = IotData.objects.all()
