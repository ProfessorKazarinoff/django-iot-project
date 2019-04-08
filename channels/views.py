# channels/views.py

from django.views.generic import ListView
from iot_data.models import IotData


class ChannelListView(ListView):
    template_name = "one_channel_listing.html"

    def get_queryset(self):
        channel_number = self.kwargs.get("channel_id")
        queryset = IotData.objects.filter(channel_num__exact=channel_number).order_by('created_at').reverse()
        return queryset

    # add extra variable into template
    def get_context_data(self, *args, **kwargs):
        channel_number = self.kwargs.get("channel_id")
        context = super(ChannelListView, self).get_context_data(*args, **kwargs)
        context['channel_number'] = channel_number
        return context


class FieldListView(ListView):
    template_name = "one_field_listing.html"

    def get_queryset(self):
        channel_number = self.kwargs.get("channel_id")
        field_number = self.kwargs.get("field_id")
        queryset = IotData.objects.filter(channel_num__exact=channel_number).filter(
            field_num__exact=field_number).order_by('created_at').reverse()
        return queryset

    # add extra variable into template
    def get_context_data(self, *args, **kwargs):
        channel_number = self.kwargs.get("channel_id")
        field_number = self.kwargs.get("field_id")
        context = super(FieldListView, self).get_context_data(*args, **kwargs)
        context['channel_number'] = channel_number
        context['field_number'] = field_number
        return context
