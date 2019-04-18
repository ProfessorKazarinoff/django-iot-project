# channels/filters.py

from iot_data.models import IotData
import django_filters

class ChannelFilter(django_filters.FilterSet):
    class Meta:
        model = IotData
        fields = ['channel_num']
