from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse
from .models import Client
from .forms import ClientForm
import json


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "clients/list.html"
    context_object_name = "clients"

    def get_queryset(self):
        objects = list(Client.objects.values("name", "phone", "annotations"))
        objects = json.dumps(objects)
        print(objects)
        return objects


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "clients/detail.html"
    context_object_name = "client"


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "clients/create.html"
    form_class = ClientForm

    def get_success_url(self):
        return reverse("clients/list.html")


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = "clients/update.html"
    fields = ["name", "phone", "annotations"]


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client

    def get_success_url(self):
        return reverse("clients/list.html")


class ClientsListView(LoginRequiredMixin, TemplateView):
    template_name = "clients/list.html"
