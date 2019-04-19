# iot_data/views.py

from django.views.generic import ListView
from .models import IotData

# Create your views here.


class IotDataPageView(ListView):
    model = IotData
    template_name = "iotdata_list.html"
