# api/read_urls.py

from django.urls import path, re_path, include

from .views import FieldListView, FieldListParameterView

urlpatterns = [
    path('data', FieldListParameterView.as_view()),
    path('channel=<int:channel_id>&field=<int:field_id>', FieldListView.as_view()),
    path('channel=<int:channel_id>&field=<int:field_id>&results=all', FieldListView.as_view()),
    # http://example.com/api/purchases?username=denvercoder9
    path('?channel=<int:channel_id>&?field=<int:field_id>', FieldListParameterView.as_view()),
]
