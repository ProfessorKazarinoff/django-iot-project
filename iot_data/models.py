# iot_data/models.py

from django.db import models

# Create your models here.

class IotData(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    channel_num = models.PositiveSmallIntegerField()
    field_num = models.PositiveSmallIntegerField()
    data = models.DecimalField(max_digits=19, decimal_places=10)
    uploaded_by = models.CharField(max_length=30)
    upload_success = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.created_at} channel: {self.channel_num} field: {self.field_num} data: {self.data}'
