# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


def register(request):
    form = UserCreationForm()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Registration'})
