from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Client
from .forms import ClientForm

class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "clients/list.html"
    context_object_name = "clients"

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "clients/detail.html"
    context_object_name = "client"

class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "clients/create.html"
    form_class = ClientForm
    success_url = reverse_lazy('list')
    # fields = ['name', 'phone', 'annotations', 'address']

class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = "clients/update.html"
    fields = ['name', 'phone', 'annotations']

class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('clients:list')
