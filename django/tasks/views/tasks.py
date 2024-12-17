from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.forms import TaskForm
from tasks.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "task/list.html"
    context_object_name = "tasks"

class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "task/detail.html"
    context_object_name = "task"

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "task/form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task:list")

class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "task/form.html"
    form_class = TaskForm
    success_url = reverse_lazy("task:list")

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "task/delete.html"
    success_url = reverse_lazy("task:list")
