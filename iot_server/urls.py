# urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("data/", include("iot_data.urls")),
    path("api/", include("api.urls")),
    path("", include("pages.urls")),
]
