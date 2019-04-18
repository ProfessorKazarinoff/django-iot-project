# iot_data/urls.py

from django.urls import path
from .views import IotDataPageView

urlpatterns = [
    path("list/", IotDataPageView.as_view(), name="datalist"),
]
