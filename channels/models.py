# channels/models.py

from django.db import models

# Create your models here.

class User(models.Model):
    email = models.CharField(max_length=100)
    username= models.CharField(max_length=100)
    api_key= models.CharField(max_length=50)

class Channel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    channel_num = models.PositiveSmallIntegerField()
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='channel')
    fields = models.CharField(max_length=30)
    allowed_users=models.ManyToManyField(User,related_name='channels')

    def __str__(self):
        return f'Channel {self.channel_num} created by: {self.created_by} with  fields: {self.fields}'
