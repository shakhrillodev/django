from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Home_Page_View(request):
    return render(request, "homepage/homepage.html")

def About_Page_View(request):
    return render(request, "about/index.html")