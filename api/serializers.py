# api/serializers.py

from rest_framework.serializers import ModelSerializer
from iot_data.models import IotData


class IotDataSerializer(ModelSerializer):
    class Meta:
        model = IotData
        fields = ("timestamp", "channel_num", "field_num", "data", "user")
