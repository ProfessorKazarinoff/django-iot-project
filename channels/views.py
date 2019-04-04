# channels/views.py

from django.shortcuts import render

from django.views.generic import ListView
from .models import Channels
from iot_data.models import IotData

# Create your views here.

class ChannelListView(ListView):
    model = IotData
    template_name = 'channel_listing.html'
