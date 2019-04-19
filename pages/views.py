# pages/views.py

from django.views.generic import TemplateView, ListView
from iot_data.models import IotData

# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class DocsPageView(TemplateView):
    template_name = "docs.html"


class LiveChartView(TemplateView):
    template_name = "livechart.html"


class ChannelListView(ListView):
    model = IotData
    paginate_by = 10
    template_name = "channels_listing.html"

    def get_queryset(self, *args, **kwargs):
        queryset = IotData.objects.values("channel_num").distinct()

        return queryset


class UserListView(ListView):
    model = IotData
    paginate_by = 10
    template_name = "users_listing.html"

    def get_queryset(self, *args, **kwargs):
        queryset = IotData.objects.values("user").distinct()

        return queryset


class OneChannelView(ListView):
    template_name = "one_channel_listing.html"

    def get_queryset(self, *args, **kwargs):
        channel_num = self.kwargs.get("channel_id")
        queryset = (
            IotData.objects.filter(channel_num__exact=channel_num)
            .order_by("timestamp")
            .reverse()
        )
        return queryset

    # add extra variable into template
    def get_context_data(self, *args, **kwargs):
        channel_num = self.kwargs.get("channel_id")
        context = super(OneChannelView, self).get_context_data(*args, **kwargs)
        context["channel_number"] = channel_num
        return context
