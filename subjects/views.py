from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

from subjects.models import Subject
from blog.models import Post


def home(request):
    context = {
        'subjects': Subject.objects.all(),
    }
    return render(request, 'subjects/home.html', context)


class SubjectListView(ListView):
    model = Subject
    template_name = 'subjects/home.html'  # antwort auf debug message von: <app>/<model>_<viewtype>.html
    context_object_name = 'subjects'
    ordering = ['-date_posted']  # order the posts. The new one first. just add '-'
    paginate_by = 5


class SubjectDetailView(DetailView):  # one post
    model = Subject


class SubjectPostListView(ListView):
    """
    all posts of a user
    """
    model = Post
    template_name = 'subjects/subject_posts.html'  # antwort auf debug message von: <app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(SubjectPostListView, self).get_context_data(**kwargs)
        context['right_sidbare'] = 'right sidebar from SubjectPostListView'
        return context

    def get_queryset(self):
        subject = get_object_or_404(Subject, id=self.kwargs.get('id'))
        return Post.objects.filter(subject=subject).order_by('-date_posted')
