from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class HomePage(TemplateView):
    template_name = 'index.html'
    
class ByePage(TemplateView):
    template_name = 'bye.html'