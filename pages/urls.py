# pages/urls.py

from django.urls import path
from .views import HomePageView, DocsPageView, LiveChartView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("docs/", DocsPageView.as_view(), name="docs"),
    path("livechart/", LiveChartView.as_view(), name="livechart"),
]
