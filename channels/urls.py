# channels/urls.py

from django.urls import path
from .views import ChannelListView, FieldListView, ChannelSummaryView

urlpatterns = [
    path("summary/", ChannelSummaryView.as_view(), name="channel_summary"),
    path('<slug:channel_id>/', ChannelListView.as_view(), name='one_channel_list'),
    path('<slug:channel_id>/field/<slug:field_id>/', FieldListView.as_view(), name='one_field_list'),
]
