# channels/urls.py

from django.urls import path
from .views import ChannelListView, createmydatabaseentry

urlpatterns = [
    path("list/", ChannelListView.as_view(), name="datalist"),
    path('entry/create/channel/<entryAttribute1>/field/<entryAttribute2>/data/<entryAttribute3>', createmydatabaseentry, name='create'),
]

# from django.urls import path
# from . import views

# urlpatterns = [
#     
#     path('api/entry/<entryID>',views.showmydatabaseentry,name='show'),
#     path('api/entry/index',views.indexdatabaseentrys,name='index'),
  
# ]
