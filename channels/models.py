# channels/models.py

from django.db import models

# Create your models here.

class Channels(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    channel_num = models.PositiveSmallIntegerField()
    created_by = models.CharField(max_length=30)
    fields = models.CharField(max_length=30)

    def __str__(self):
        return f'Channel {self.channel_num} created by: {self.created_by} with  fields: {self.fields}'
