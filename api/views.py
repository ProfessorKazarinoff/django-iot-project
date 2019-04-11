# api/views.py

from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from iot_data.models import IotData
from .serializers import IotDataSerializer

from django.views.generic import DetailView, ListView
from django.http import HttpResponse, JsonResponse
from django_filters.rest_framework import DjangoFilterBackend


def create_db_entry(request, api_key_str, channel_pk, field_pk, data_str):
    """
    function-based view to write a data point to the database
    """
    if api_key_str == 'ABC':
        entry = IotData.objects.create(channel_num=int(channel_pk), field_num=int(field_pk), data=float(data_str),
                                       uploaded_by='peter')
        # return HttpResponse('<h1>Success</h1>')
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


def latest_data_point_view(request, channel_pk):
    # latest_entry = IotData.objects.latest('created_at')
    # result = IotData.objects.all()
    entry = IotData.objects.last()
    # response_dict = dict(result)
    # queryset = IotData.objects.all()
    # latest_entry = queryset.objects.latest('created_at')
    # add your serializer
    # serializer_class = IotDataSerializer
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

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """
    def get_object(self):
        queryset = self.get_queryset()             # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]: # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class DataViewSet(GenericViewSet,  # generic view functionality
                  CreateModelMixin,  # handles POSTs
                  RetrieveModelMixin,  # handles GETs for 1 data point
                  UpdateModelMixin,  # handles PUTs and PATCHes
                  ListModelMixin):  # handles GETs for many data points

    serializer_class = IotDataSerializer
    queryset = IotData.objects.all()

class FieldListView(ListAPIView):
    serializer_class = IotDataSerializer
    def get_queryset(self):
        channel_id = self.kwargs.get("channel_id")
        field_id = self.kwargs.get("field_id")
        return IotData.objects.filter(channel_num=channel_id).filter(field_num=field_id)

class FieldListParameterView(ListAPIView):
    queryset = IotData.objects.all()
    serializer_class = IotDataSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('channel_num', 'field_num')
