# api/urls.py

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import DataViewSet, DataListView, create_db_entry

router = DefaultRouter()
router.register("", DataViewSet, base_name="data")

urlpatterns = [
    path("read/", DataListView.as_view()),
    path("write/", create_db_entry, name="create_db_entry_wotj ampersand"),
    path("", include(router.urls)),
]
