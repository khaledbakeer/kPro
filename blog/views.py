# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
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

    # show 5 posts per page, you can navigate manuel like : http://127.0.0.1:8000/?page=3
    # this will show the third page
    paginate_by = 5


class UserPostListView(ListView):
    """
    all posts of a user
    """
    model = Post
    template_name = 'blog/user_posts.html'  # antwort auf debug message von: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    # ordering = ['-date_posted']  # order the posts. The new one first. just add '-'

    # show 5 posts per page, you can navigate manuel like : http://127.0.0.1:8000/?page=3
    # this will show the third page
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):  # one post
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):  # to view new post have to be logged in
    model = Post
    fields = ['title', 'content', 'subject']

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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     DeleteView):  # have to be logged in to be able to delete posts
    model = Post
    success_url = '/'

    def test_func(self):  # to be sure that the user edit just his posts
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    # return HttpResponse('<h1>Blog About Page</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
