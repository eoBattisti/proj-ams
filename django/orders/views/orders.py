import datetime as dt
import json
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db import transaction
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from orders.forms import OrderForm
from orders.models import Order
from tasks.forms import TaskFormSet
from tasks.models import Task


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/list.html"
    context_object_name = "orders"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_objects"] = Order.objects.count()
        return context


class OrderListJsonView(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        objects: QuerySet[Order, Order] = super().get_queryset()
        return objects

    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        page_number = self.request.GET.get("page", 1)
        page_size = self.request.GET.get("pageSize", 10)

        paginator = Paginator(self.get_queryset(), page_size)
        page_obj = paginator.get_page(page_number)

        # Prepare data for Grid.js
        data = [
            {
                "client": obj.client.name,
                "due_date": str(obj.due_date),
                "order_date": str(obj.order_date),
                "total": float(obj.total),
                "completed": obj.completed,
                "discount": obj.discount,
                "id": str(obj.id),
            }
            for obj in page_obj
        ]

        response_data = {
            "data": data,
            "total": paginator.count,
        }

        return HttpResponse(json.dumps(response_data), content_type="application/json")


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/detail.html"
    context_object_name = "order"


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = "orders/form.html"
    success_url = reverse_lazy("orders:list")

    def get(self, request, *args, **kwargs):
        order_form = OrderForm()
        task_formset = TaskFormSet(queryset=Task.objects.none(), prefix="tasks")

        return render(request, self.template_name, {"form": order_form, "task_formset": task_formset})

    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        order_form = OrderForm(request.POST)
        task_formset = TaskFormSet(request.POST, prefix="tasks")

        if order_form.is_valid() and task_formset.is_valid():
            try:
                with transaction.atomic():
                    order = order_form.save()
                    tasks = task_formset.save(commit=False)
                    for task in tasks:
                        task.save()

                    order.tasks.add(*tasks)

                    for deleted_task in task_formset.deleted_objects:
                        deleted_task.delete()

                return redirect(self.success_url)
            except Exception as e:
                print(e)
                pass

        return render(request, self.template_name, {"form": order_form, "task_formset": task_formset})


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = "orders/form.html"
    success_url = reverse_lazy("orders:list")

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        order_form = OrderForm(request.POST, instance=self.object)
        order_form = OrderForm(instance=self.object)
        task_formset = TaskFormSet(queryset=self.object.tasks.all(), prefix="tasks")

        return render(request, self.template_name, {"form": order_form, "task_formset": task_formset})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        order_form = OrderForm(request.POST, instance=self.object)
        task_formset = TaskFormSet(
            request.POST,
            prefix="tasks",
            queryset=self.object.tasks.all(),  # Use the correct related name
        )

        if order_form.is_valid() and task_formset.is_valid():
            try:
                with transaction.atomic():
                    order = order_form.save()

                    tasks = task_formset.save(commit=False)

                    for task in tasks:
                        task.save()

                    order.tasks.add(*tasks)

                    for deleted_task in task_formset.deleted_objects:
                        print(deleted_task)
                        deleted_task.delete()

                    return redirect(self.success_url)
            except Exception as e:
                print(f"Error: {e}")

        return render(request, self.template_name, {"form": order_form, "task_formset": task_formset})


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "orders/delete.html"
    success_url = reverse_lazy("orders:list")
