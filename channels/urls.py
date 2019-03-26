# channels/urls.py

from django.urls import path
from .views import ChannelListView

urlpatterns = [
    path("list/", ChannelListView.as_view(), name="datalist"),
]
