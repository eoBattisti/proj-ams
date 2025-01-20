from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from garments.models import Material
from garments.forms import MaterialForm


class MaterialCreateView(LoginRequiredMixin, CreateView):
    model = Material
    template_name = "materials/form.html"
    success_url = reverse_lazy("materials:list")
    form_class = MaterialForm


class MaterialDetailView(LoginRequiredMixin, DetailView):
    model = Material
    template_name = "materials/detail.html"
    context_object_name = "material"


class MaterialListView(LoginRequiredMixin, ListView):
    model = Material
    template_name = "materials/list.html"
    context_object_name = "materials"
    ordering = ["name"]


class MaterialUpdateView(LoginRequiredMixin, UpdateView):
    model = Material
    template_name = "materials/form.html"
    success_url = reverse_lazy("materials:list")
    form_class = MaterialForm
