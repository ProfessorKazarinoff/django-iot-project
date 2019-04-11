# api/read_urls.py

from django.urls import path, re_path

from .views import FieldListView, ChannelList, ChannelQueryList

urlpatterns = [
    path('channel=<int:channel_id>&field=<int:field_id>', FieldListView.as_view()),
    path('channel=<int:channel_id>&field=<int:field_id>&results=all', FieldListView.as_view()),
    # http://example.com/api/purchases?username=denvercoder9
    re_path('^channel/(?P<channel_id>.+)/$', ChannelList.as_view()),
    re_path('^query/', ChannelQueryList.as_view()),
]
