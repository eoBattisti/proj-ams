import json
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from tasks.forms import TaskForm
from tasks.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list.html"
    context_object_name = "tasks"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_objects"] = Task.objects.count()
        return context


class TaskListJsonView(LoginRequiredMixin, ListView):
    model = Task

    def get_queryset(self):
        objects: QuerySet[Task, Task] = super().get_queryset()
        return objects

    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        page_number = self.request.GET.get("page", 1)
        page_size = self.request.GET.get("pageSize", 10)

        paginator = Paginator(self.get_queryset(), page_size)
        page_obj = paginator.get_page(page_number)

        # Prepare data for Grid.js
        data = [
            {
                "description": obj.description,
                "value": float(obj.value),
                "task_type": str(obj.task_type),
                "id": str(obj.id),
            }
            for obj in page_obj
        ]

        response_data = {
            "data": data,
            "total": paginator.count,
        }

        return HttpResponse(json.dumps(response_data), content_type="application/json")


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    context_object_name = "task"


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:list")


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = "tasks/form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:list")
