# channels/views.py

from django.views.generic import ListView
from iot_data.models import IotData
#from channels.models import Channel


class ChannelListView(ListView):
    template_name = "one_channel_listing.html"

    def get_queryset(self, *args, **kwargs):
        channel_num = self.kwargs.get("channel_id")
        queryset = IotData.objects.filter(channel_num__exact=channel_num).order_by('timestamp').reverse()
        return queryset

    # add extra variable into template
    def get_context_data(self, *args, **kwargs):
        channel_num = self.kwargs.get("channel_id")
        context = super(ChannelListView, self).get_context_data(*args, **kwargs)
        context['channel_number'] = channel_num
        return context


class FieldListView(ListView):
    template_name = "one_field_listing.html"

    # only pull out data from one channel and one field
    def get_queryset(self, *args, **kwargs):
        channel_num = self.kwargs.get("channel_id")
        field_num = self.kwargs.get("field_id")
        queryset = IotData.objects.filter(channel_num__exact=channel_num).filter(
            field_num__exact=field_num).order_by('timestamp').reverse()
        return queryset

    # add extra variable into template
    def get_context_data(self, *args, **kwargs):
        channel_num = self.kwargs.get("channel_id")
        field_num = self.kwargs.get("field_id")
        context = super(FieldListView, self).get_context_data(*args, **kwargs)
        context['channel_number'] = channel_num
        context['field_number'] = field_num
        return context

class ChannelSummaryView(ListView):
    template_name = "docs.html"
    
    model = IotData
