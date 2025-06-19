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
from tasks.forms import TaskTypeForm
from tasks.models import TaskType


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "task_types/list.html"
    context_object_name = "task_types"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_objects"] = TaskType.objects.count()
        return context


class TaskTypeListJsonView(LoginRequiredMixin, ListView):
    model = TaskType

    def get_queryset(self):
        objects: QuerySet[TaskType, TaskType] = super().get_queryset()
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
                "value": float(obj.base_value),
                "id": str(obj.id),
            }
            for obj in page_obj
        ]

        response_data = {
            "data": data,
            "total": paginator.count,
        }

        return HttpResponse(json.dumps(response_data), content_type="application/json")


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
