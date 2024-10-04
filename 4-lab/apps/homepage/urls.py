from .views import Home_Page_View, About_Page_View
from django.urls import path

urlpatterns = [
    path('about/', About_Page_View.as_view(),name='about'),
    path('', Home_Page_View,name='homepage'),
]