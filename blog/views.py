# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>Blog About Page</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
