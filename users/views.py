# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created for ' + username + '!')
            # messages.debug()
            # messages.info()
            # messages.error()
            # messages.success()
            # messages.warning()
            return redirect('blog_homePage')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/registration.html', {'form': form, 'title': 'Registration'})
