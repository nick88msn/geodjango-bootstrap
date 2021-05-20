from django.shortcuts import render

# Adding TemplateView
from django.views.generic.base import TemplateView

# Create your views here.

class MarkersMapView(TemplateView):
    template_name = 'map.html'