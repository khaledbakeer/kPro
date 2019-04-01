from __future__ import unicode_literals
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    subject_name = models.CharField(max_length=255)

    subject_number = models.CharField(max_length=50)

    responsible_lecturer_name = models.CharField(max_length=50)

    responsible_lecturer_email = models.EmailField()

    content_and_goals = models.TextField()

    teaching_and_learning_forms = models.TextField()

    requirements_for_participation = models.TextField()

    usability = models.TextField()

    requirements_for_the_award_of_credit_points = models.TextField()

    credits_and_grades = models.TextField()

    frequency_of_the_module = models.TextField()

    workload = models.TextField()

    duration_of_the_module = models.TextField()

    date_updated = models.DateTimeField(auto_now=True)

    date_posted = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject_name
