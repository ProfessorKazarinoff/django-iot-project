# api/urls.py

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import IoTDataList, IoTDataDetail, DataViewSet

router = DefaultRouter()
router.register('data',DataViewSet, base_name='data')

urlpatterns = [
    path('', IoTDataList.as_view()),
    path('<int:pk>/', IoTDataDetail.as_view()),
    re_path('^', include(router.urls)),
]
