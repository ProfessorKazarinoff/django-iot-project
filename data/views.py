# data/views.py
from django.utils import timezone
from django.shortcuts import render

from django.views.generic import ListView
from .models import Data

# Create your views here.

class DataPageView(ListView):
    model = Data
    template_name = 'datapage.html'
