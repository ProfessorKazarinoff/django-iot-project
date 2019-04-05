# channels/urls.py

from django.urls import path
from .views import ChannelListView

urlpatterns = [
    path("list/", ChannelListView.as_view(), name="datalist"),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     path('api/entry/create/<entryAttribute1>/<entryAttribute2>',views.createmydatabaseentry,name='create'),
#     path('api/entry/<entryID>',views.showmydatabaseentry,name='show'),
#     path('api/entry/index',views.indexdatabaseentrys,name='index'),
  
# ]
