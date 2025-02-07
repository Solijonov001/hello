from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePagesView(TemplateView):
    template_name = 'home.html'

class AboutPagesView(TemplateView):
    template_name = 'about.html'

class NewsPagesView(TemplateView):
    template_name = 'news.html'

class OutherPagesView(TemplateView):
    template_name = 'author.html'

