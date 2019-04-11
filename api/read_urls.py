# api/read_urls.py

from django.urls import path, re_path, include

from .views import FieldListView

urlpatterns = [
    path('channel=<int:channel_id>&field=<int:field_id>', FieldListView.as_view()),
    path('channel=<int:channel_id>&field=<int:field_id>&results=all', FieldListView.as_view()),
]
