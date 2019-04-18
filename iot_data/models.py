# iot_data/models.py

from django.db import models
from channels.models import Channel
from users.models import User


class IotData(models.Model):
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE,related_name='iotdata')
    timestamp = models.DateTimeField(auto_now_add=True)
    field_num = models.PositiveSmallIntegerField()
    data = models.DecimalField(max_digits=19, decimal_places=10)
    uploaded_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='iotdata')

    def __str__(self):
        return f'{self.timestamp} channel: {self.channel_num} field: {self.field_num} data: {self.data}'
