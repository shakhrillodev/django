from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def Home_Page_View(request):
    return render(request, "homepage.html")

class About_Page_View(TemplateView):
    template_name =  "about.html"