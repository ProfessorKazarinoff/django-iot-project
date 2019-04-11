# api/urls.py

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import IoTDataList, IoTDataDetail, DataViewSet, create_db_entry, latest_data_point_view

router = DefaultRouter()
router.register('data', DataViewSet, base_name='data')

urlpatterns = [
    path('', IoTDataList.as_view()),
    path('<int:pk>/', IoTDataDetail.as_view()),
    re_path('^', include(router.urls)),
    path('write/api_key=<str:api_key_str>/channel=<int:channel_pk>/field=<int:field_pk>/data=<str:data_str>', create_db_entry, name='create_db_entry'),
    path('channel=<channel_pk>/latest', latest_data_point_view, name='latest_db_entry'),
    path('read/', include('api.read_urls')),
]
