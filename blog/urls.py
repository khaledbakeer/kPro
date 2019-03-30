from django.urls import path
from . import views

urlpatterns = [
    path('about', views.about, name='blog_aboutPage'),
    path('', views.home, name='blog_homePage'),
]
