from django.urls import reverse_lazy

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from orders.forms import OrderForm
from orders.models import Order


class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = "orders/list.html"
    context_object_name = "orders"


class OrderDetailView(LoginRequiredMixin, DetailView):
    model = Order
    template_name = "orders/detail.html"
    context_object_name = "order"


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    template_name = "orders/form.html"
    form_class = OrderForm
    success_url = reverse_lazy("orders:list")


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = "orders/form.html"
    form_class = OrderForm
    success_url = reverse_lazy("orders:list")


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "orders/delete.html"
    success_url = reverse_lazy("orders:list")
