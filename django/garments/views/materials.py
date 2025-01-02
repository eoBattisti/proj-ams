from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from garments.models import Material


class MaterialCreateView(CreateView):
    model = Material
    template_name = "materials/form.html"
    success_url = reverse_lazy("materials:list")


class MaterialDetailView(DetailView):
    model = Material
    template_name = "materials/detail.html"
    context_object_name = "garment"


class MaterialListView(ListView):
    model = Material
    template_name = "materials/list.html"
    context_object_name = "materials"
    ordering = ["name"]


class MaterialUpdateView(UpdateView):
    model = Material
    template_name = "materials/form.html"
    success_url = reverse_lazy("materials:list")
