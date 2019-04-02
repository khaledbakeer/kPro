from django.urls import path
from subjects.views import SubjectListView, SubjectDetailView, SubjectPostListView

urlpatterns = [
    path('', SubjectListView.as_view(), name='subject_homePage'),
    path('<int:pk>/', SubjectDetailView.as_view(), name='subject_detail'),
    path('<int:id>/posts/', SubjectPostListView.as_view(), name='subject_posts'),
]
