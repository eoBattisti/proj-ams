from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from garments.forms import GarmentForm
from garments.models import Garment


class GarmentCreateView(CreateView):
    model = Garment
    template_name = "garments/form.html"
    success_url = reverse_lazy("garments:list")
    form_class = GarmentForm


class GarmentDetailView(DetailView):
    model = Garment
    template_name = "garments/detail.html"
    context_object_name = "garment"


class GarmentListView(ListView):
    model = Garment
    template_name = "garments/list.html"
    context_object_name = "garments"
    ordering = ["name"]


class GarmentUpdateView(UpdateView):
    model = Garment
    template_name = "garments/form.html"
    success_url = reverse_lazy("garments:list")
    form_class = GarmentForm
