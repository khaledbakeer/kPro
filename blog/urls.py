from django.conf.urls import url
import views

urlpatterns = [
    url('', views.home, name='blog_homePage'),
    url('about/', views.about, name='blog_aboutPage'),
]
