from django.views.generic import CreateView, DetailView, ListView, UpdateView

from sales.models import Sale


class SaleListView(ListView):
    model = Sale
    template_name = "sales/list.html"
    context_object_name = "sales"


class SaleCreateView(CreateView):
    model = Sale
    fields = ["client", "garment", "quantity", "total", "saled_at"]
    template_name = "sales/form.html"


class SaleUpdateView(UpdateView):
    model = Sale
    fields = ["client", "garment", "quantity", "total", "saled_at"]
    template_name = "sales/form.html"


class SaleDetailView(DetailView):
    model = Sale
    template_name = "sales/detail.html"
    context_object_name = "sale"
