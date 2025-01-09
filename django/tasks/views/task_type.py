from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from tasks.forms import TaskTypeForm
from tasks.models import TaskType


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "task_types/list.html"
    context_object_name = "task_types"


class TaskTypeDetailView(LoginRequiredMixin, DetailView):
    model = TaskType
    template_name = "task_types/detail.html"
    context_object_name = "task_types"


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task_types/form.html"
    success_url = reverse_lazy("task_types:list")


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task_types/form.html"
    success_url = reverse_lazy("task_types:list")


class TaskTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = TaskType
    template_name = "task_types/task_type_confirm_delete.html"
    success_url = reverse_lazy("task_types:list")
