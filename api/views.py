# api/views.py

from django.views.generic import DetailView
from django.http import HttpResponse, JsonResponse

from rest_framework import generics
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.pagination import LimitOffsetPagination

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
    except:
        return HttpResponse('<h1>invalid request</h1>',status=400)

    else:
        return HttpResponse('<h1>invalid api key</h1>')


class LatestDataView(RetrieveAPIView):
    queryset = IotData.objects.all()
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


class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
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


class ChannelList(generics.ListAPIView):
    serializer_class = IotDataSerializer

    def get_queryset(self):
        queryset = IotData.objects.all()
        channel_id = self.kwargs['channel_id']
        field_id = self.request.query_params.get('field', None)
        if field_id is not None:
            queryset = queryset.filter(channel_num=channel_id).filter(field_num=field_id)
        else:
            queryset = queryset.filter(channel_num=channel_id)
        return queryset


class ChannelQueryList(generics.ListAPIView):
    serializer_class = IotDataSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        queryset = IotData.objects.all()
        channel_id = self.request.query_params.get('channel', None)
        field_id = self.request.query_params.get('field', None)
        if field_id is not None and channel_id is not None:
            queryset = queryset.filter(channel_num=channel_id).filter(field_num=field_id).order_by('timestamp').reverse()
        elif field_id is not None and channel_id is None:
            queryset = queryset.filter(field_num=field_id).order_by('timestamp').reverse()
        elif channel_id is not None and field_id is None:
            queryset = queryset.filter(channel_num=channel_id).order_by('timestamp').reverse()
        return queryset
