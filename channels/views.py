# channels/views.py

from django.shortcuts import render

from django.views.generic import ListView
from .models import Channels

# Create your views here.

class ChannelListView(ListView):
    model = Channels
    template_name = 'channel_listing.html'
