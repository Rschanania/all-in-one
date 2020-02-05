from django.shortcuts import render
from django.views.generic import TemplateView
class cbview(TemplateView):
    template_name = 'collage/collage_view.html'