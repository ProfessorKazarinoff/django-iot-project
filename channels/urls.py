# channels/urls.py

from django.urls import path
from .views import ChannelListView #, createmydatabaseentry

urlpatterns = [
    path("list/", ChannelListView.as_view(), name="datalist"),
    path('list/<slug:channel_id>/', ChannelListView.as_view(), name='channel_list'),
    path('<slug:channel_id>/', ChannelListView.as_view(), name='one_channel_list'),
    #path('entry/create/channel/<entryAttribute1>/field/<entryAttribute2>/data/<entryAttribute3>', createmydatabaseentry, name='create'),
]
