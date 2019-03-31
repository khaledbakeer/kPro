from django.urls import path
from . import views
from .views import PostListView, PostDetailView

urlpatterns = [
    path('', PostListView.as_view(), name='blog_homePage'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('about', views.about, name='blog_aboutPage'),

]
