# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'title': 'first Post',
        'author': 'John Smith',
        'post_date': '01.02.1999',
        'content': 'content of first post'
    },
    {
        'title': 'sevond Post',
        'author': 'John SS',
        'post_date': '02.05.2005',
        'content': 'content of second post'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>Blog About Page</h1>')
    return render(request, 'blog/about.html', {'title': 'About'})
