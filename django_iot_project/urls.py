# urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("pages.urls")),
    path("data/", include("iot_data.urls")),
    path("api/", include("api.urls")),
    path("channel/", include("channels.urls")),
]
