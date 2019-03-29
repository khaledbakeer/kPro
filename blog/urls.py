from django.conf.urls import url
import views

urlpatterns = [
    url('about', views.about, name='blog_aboutPage'),
    url('', views.home, name='blog_homePage'),
]
