# iot_data/admin.py

from django.contrib import admin

# Register your models here.

from .models import IotData


admin.site.register(IotData)
