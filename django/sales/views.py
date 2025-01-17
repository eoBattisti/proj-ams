from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from sales.models import Sale


class SaleListView(LoginRequiredMixin, ListView):
    model = Sale
    template_name = "sales/list.html"
    context_object_name = "sales"


class SaleCreateView(LoginRequiredMixin, CreateView):
    model = Sale
    fields = ["client", "garment", "quantity", "total", "saled_at"]
    template_name = "sales/form.html"


class SaleUpdateView(LoginRequiredMixin, UpdateView):
    model = Sale
    fields = ["client", "garment", "quantity", "total", "saled_at"]
    template_name = "sales/form.html"


class SaleDetailView(LoginRequiredMixin, DetailView):
    model = Sale
    template_name = "sales/detail.html"
    context_object_name = "sale"
