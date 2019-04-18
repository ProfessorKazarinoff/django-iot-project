# channels/admin.py

from django.contrib import admin

# Register your models here.

from .models import Channel


admin.site.register(Channel)
