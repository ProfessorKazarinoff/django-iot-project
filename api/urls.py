# api/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.IoTDataList.as_view()),
    path('<int:pk>/', views.IoTDataDetail.as_view()),
]
