# channels/urls.py

from django.urls import path
from .views import ChannelListView, FieldListView

urlpatterns = [
    path("list/", ChannelListView.as_view(), name="datalist"),
    path('list/<slug:channel_id>/', ChannelListView.as_view(), name='channel_list'),
    path('<slug:channel_id>/', ChannelListView.as_view(), name='one_channel_list'),
    path('<slug:channel_id>/field/<slug:field_id>/', FieldListView.as_view(), name='one_field_list'),
]
