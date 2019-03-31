from django.urls import path
from . import views
from .views import PostListView

urlpatterns = [
    path('about', views.about, name='blog_aboutPage'),
    path('', PostListView.as_view(), name='blog_homePage'),
]
