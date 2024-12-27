# from django.shortcuts import render
# from django.http import HttpResponse
# import random

from django.views.generic import ListView
from task.models import Task
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from task.forms import TaskForm

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')
        if category:
            queryset = queryset.filter(category__name=category)
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset
from .models import Category

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        search = self.request.GET.get('search')
        if category:
            queryset = queryset.filter(category__name=category)
        if search:
            queryset = queryset.filter(title__icontains=search)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'
    context_object_name = 'task'


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/task_form.html'
    success_url = '/tasks/'

