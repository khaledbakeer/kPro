# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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


class PostCreateView(LoginRequiredMixin, CreateView):  # to view new post have to be logged in
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # to view new post have to be logged in
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):  # to be sure that the user edit just his posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    # return HttpResponse('<h1>Blog About Page</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
