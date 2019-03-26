# api/serializers.py

from rest_framework import serializers
from iot_data.models import IotData


class IotDataSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('channel_num', 'field_num', 'data', 'uploaded_by',)
        model = IotData
