# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return HttpResponse('<h1>Blog About Page</h1>')
