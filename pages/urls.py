# pages/urls.py

from django.urls import path
from .views import (
    HomePageView,
    DocsPageView,
    LiveChartView,
    ChannelListView,
    OneChannelView,
    UserListView,
)

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("docs/", DocsPageView.as_view(), name="docs"),
    path("channel/<int:channel_id>/", OneChannelView.as_view(), name="one_channel"),
    path("channels/", ChannelListView.as_view(), name="channel_list"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("livechart/", LiveChartView.as_view(), name="livechart"),
]
