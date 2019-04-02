# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from subjects.models import Subject


class Post(models.Model):
    title = models.CharField(max_length=255)

    content = models.TextField()

    date_updated = models.DateTimeField(auto_now=True)

    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})
