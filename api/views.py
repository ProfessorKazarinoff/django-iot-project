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

from channels.models import User, Channel

from django.views.generic import DetailView
from django.http import HttpResponse, JsonResponse


def create_db_entry(request):
    """
    function-based view to write a data point to the database
    """
    if request.method =='POST':
        params=request.POST.dict()
    else:
        params=request.GET.dict()
    try:
        requester=User.objects.get(api_key=params['api_key'])
    except:
        return HttpResponse('<h1>invalid api key</h1>')
    try:
        channel=Channel.objects.get(pk=params['channel_pk'])    
    except:
        return HttpResponse('<h1>channel not found</h1>')
    if (requester in channel.allowed_users):
        entry = IotData.objects.create(channel=channel, field_num=params['field_pk'], data=params['data_str'],
                                       uploaded_by=requester)
        # return HttpResponse('<h1>Success</h1>')
        return JsonResponse(params)

    else:
        return HttpResponse('<h1>invalid api key</h1>')


class LatestDataView(RetrieveAPIView):
    queryset = IotData.objects.all()
    # add your serializer
    serializer_class = IotDataSerializer

    def get_object(self, *args, **kwargs):
        return self.queryset.filter(channel_num=kwargs.get('channel_pk')).latest('timestamp')


def latest_data_point_view(request, channel_pk):
    entry = IotData.objects.last()
    entrydict = {
        'id': entry.id,
        'channel': entry.channel_num,
        'field': entry.field_num,
        'data': entry.data}
    return JsonResponse(entrydict)


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
