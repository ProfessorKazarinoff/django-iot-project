# channels/views.py

from django.shortcuts import render
# what we're going to return when a request is sent
from django.http import JsonResponse
from django.views.generic import ListView
from .models import Channels
from iot_data.models import IotData
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .filters import ChannelFilter

class ChannelListView(ListView):

    model = IotData
    template_name = "one_channel_listing.html"
    slug_url_kwarg = "channel_id"

    

    def get_context_data(self, *args, **kwargs):
        context = super(ChannelListView, self).get_context_data(*args, **kwargs)
        context['channel_number'] = 2
        return context