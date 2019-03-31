# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # antwort auf debug message von: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']  # order the posts. The new one first. just add '-'


class PostDetailView(DetailView):  # one post
    model = Post


class PostCreateView(CreateView):  # one post
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    # return HttpResponse('<h1>Blog About Page</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
