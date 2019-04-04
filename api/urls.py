# api/urls.py

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from .views import IoTDataList, IoTDataDetail, DataViewSet, IoTDataPointDetail

# see https://docs.djangoproject.com/en/2.2/topics/http/urls/#path-converters 
# for how to include <int:pk>, <str:string>

router = DefaultRouter()
router.register('data', DataViewSet, base_name='data')

urlpatterns = [
    path('', IoTDataList.as_view()),
    path('<int:pk>/', IoTDataDetail.as_view()),
    re_path('^', include(router.urls)),
    #path('channel/<int:pk>/field/1/', IoTDataPointDetail.as_view())
    path('channel/', include('channels.urls'))
]
