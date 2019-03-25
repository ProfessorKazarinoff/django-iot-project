# data/admin.py

from django.contrib import admin

# Register your models here.

from .models import Data


admin.site.register(Data)
