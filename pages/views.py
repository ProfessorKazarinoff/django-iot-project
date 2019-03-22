# pages/views.py

from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class DocsPageView(TemplateView):
    template_name = 'docs.html'
