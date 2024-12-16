from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from orders.forms import OrderTypeForm
from orders.models import OrderType


class OrderTypeListView(LoginRequiredMixin, ListView):
    model = OrderType
    template_name = "order_types/list.html"
    context_object_name = "order_types"


class OrderTypeDetailView(LoginRequiredMixin, DetailView):
    model = OrderType
    template_name = "order_types/detail.html"
    context_object_name = "order_type"


class OrderTypeCreateView(LoginRequiredMixin, CreateView):
    model = OrderType
    form_class = OrderTypeForm
    template_name = "order_types/form.html"
    success_url = reverse_lazy("order_types:list")


class OrderTypeUpdateView(LoginRequiredMixin, UpdateView):
    model = OrderType
    form_class = OrderTypeForm
    template_name = "order_types/form.html"
    success_url = reverse_lazy("order_types:list")


class OrderTypeDeleteView(LoginRequiredMixin, DeleteView):
    model = OrderType
    template_name = "order_types/order_type_confirm_delete.html"
    success_url = reverse_lazy("order_types:list")
