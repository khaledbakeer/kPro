from django.shortcuts import render
from django.views.generic import ListView, DetailView

from subjects.models import Subject


def home(request):
    context = {
        'subjects': Subject.objects.all()
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
