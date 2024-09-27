from django.urls import path
from .views import Home_Page_View, About_Page_View

urlpatterns = [
    path('about/', About_Page_View,name='about'),
    path('', Home_Page_View,name='homepage'),
]