# data/urls.py

from django.urls import path
from .views import DataPageView

urlpatterns = [
    path("datapage/", DataPageView.as_view(), name="datapage"),
]
