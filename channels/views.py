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
    # don't need model attribute defined if queryset attribute is defined
    # model = IotData
    template_name = "one_channel_listing.html"

    # Try to pull out the channel number from the URL


    # specify the list of object from the model with by defining a queryset
    # queryset = IotData.objects.all()
    
    # speficy a subset of the object from the model by defining a query set with a filter
    queryset = IotData.objects.filter(channel_num__exact=5).order_by('created_at').reverse()

    #add extra variable into template
    def get_context_data(self, *args, **kwargs):
        context = super(ChannelListView, self).get_context_data(*args, **kwargs)
        context['channel_number'] = 5
        return context