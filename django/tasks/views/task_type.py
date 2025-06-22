from typing import Any

from django.db.models.query import Q
from django.core.paginator import Page
from django.db.models import Avg
from django.db.models import Max
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from tasks.forms import TaskTypeForm
from tasks.models import TaskType


class TaskTypeListView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "task_types/list.html"
    context_object_name = "task_types"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        page_number: int = self.request.GET.get("page", 1)
        clients = TaskType.objects.all()

        paginator: Paginator = Paginator(clients, self.paginate_by)
        page_obj: Page = paginator.get_page(page_number)

        context.update(
            {
                "page_obj": page_obj,
            }
        )

        return context


class TaskTypeHTMXStatsView(LoginRequiredMixin, TemplateView):
    template_name = "task_types/components/stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_task_types"] = TaskType.objects.count()
        context["avg_base_value"] = TaskType.objects.all().aggregate(Avg("base_value")).get("base_value__avg", 0)
        context["highest_base_value"] = TaskType.objects.all().aggregate(Max("base_value")).get("base_value__max", 0)
        return context


class TaskTypeListHTMXView(LoginRequiredMixin, ListView):
    model = TaskType
    template_name = "task_types/components/rows.html"
    context_object_name = "task_types"
    paginate_by = 10

    def get_context_data(self, **kwargs: Any) -> HttpResponse:
        search = self.request.GET.get("search")
        context = super().get_context_data(**kwargs)
        task_types = super().get_queryset()
        page_number = self.request.GET.get("page", 1)

        if search:
            task_types = TaskType.objects.filter(Q(description__icontains=search))

        paginator = Paginator(task_types, self.paginate_by)
        page_obj = paginator.get_page(page_number)

        context[self.context_object_name] = page_obj

        return context


class TaskTypeDetailView(LoginRequiredMixin, DetailView):
    model = TaskType
    template_name = "task_types/detail.html"
    context_object_name = "task_type"


class TaskTypeCreateView(LoginRequiredMixin, CreateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task_types/form.html"
    success_url = reverse_lazy("task_types:htmx")

    def form_valid(self, form):
        try:
            self.object = form.save()
            if not self._is_htmx_request():
                return super().form_valid(form)

            response = HttpResponse()
            response["HX-Trigger"] = "closeModal"
            return response

        except Exception as e:
            print(e)

    def _is_htmx_request(self):
        return self.request.headers.get("HX-Request") == "true"


class TaskTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = TaskType
    form_class = TaskTypeForm
    template_name = "task_types/form.html"
    success_url = reverse_lazy("task_types:htmx")

    def form_valid(self, form):
        try:
            self.object = form.save()
            if not self._is_htmx_request():
                return super().form_valid(form)

            response = HttpResponse()
            response["HX-Trigger"] = "closeModal"
            return response

        except Exception as e:
            print(e)

    def _is_htmx_request(self):
        return self.request.headers.get("HX-Request") == "true"
