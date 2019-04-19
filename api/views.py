# api/views.py

from django.http import JsonResponse

from rest_framework import generics
from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from iot_data.models import IotData
from .serializers import IotDataSerializer


class DataViewSet(
    GenericViewSet,  # generic view functionality
    CreateModelMixin,  # handles POSTs
    RetrieveModelMixin,  # handles GETs for 1 data point
    UpdateModelMixin,  # handles PUTs and PATCHes
    ListModelMixin,
):  # handles GETs for many data points

    serializer_class = IotDataSerializer
    queryset = IotData.objects.all()


class DataListView(generics.ListAPIView):
    serializer_class = IotDataSerializer

    def get_queryset(self, *args, **kwargs):
        channel = self.request.query_params.get("channel", None)
        field = self.request.query_params.get("field", None)
        queryset = IotData.objects.all()
        if (channel is not None) and (field is not None):
            queryset = (
                queryset.filter(channel_num__exact=channel)
                .filter(field_num__exact=field)
                .order_by("timestamp")
                .reverse()
            )
        elif channel is not None:
            queryset = (
                queryset.filter(channel_num__exact=channel)
                .order_by("timestamp")
                .reverse()
            )
        elif field is not None:
            queryset = (
                queryset.filter(field_num__exact=field).order_by("timestamp").reverse()
            )
        return queryset


def create_db_entry(request):
    """
    function-based view to write a data point to the database
    """
    if request.method == "POST":
        params = request.POST.dict()
    else:
        params = request.GET.dict()
    entry = IotData.objects.create(
        channel_num=params["channel"], field_num=params["field"], data=params["data"]
    )

    return JsonResponse(params)
