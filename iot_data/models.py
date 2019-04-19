# iot_data/models.py

from django.db import models


class IotData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    channel_num = models.PositiveSmallIntegerField()
    field_num = models.PositiveSmallIntegerField()
    data = models.DecimalField(max_digits=19, decimal_places=10)
    user = models.CharField(max_length=50, default="peter")

    def __str__(self):
        return f"{self.timestamp} channel: {self.channel_num} field: {self.field_num} data: {self.data}"
