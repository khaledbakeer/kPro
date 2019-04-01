from django.urls import path
from subjects.views import SubjectListView

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_homePage'),
]
