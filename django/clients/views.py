from django.shortcuts import render
from urllib import request
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy
from .models import Client

class ClientListView(ListView):
    model = Client
    template_name = "list.html"
    context_object_name = "clients"
    
class ClientDetailView(DetailView):
    model = Client
    template_name = "detail.html"
    context_object_name = "clients"
    
class ClientCreateView(CreateView):
    model = Client
    template_name = "create.html"
    fields = ['name', 'phone', 'annotations', 'address']
    
class ClientUpdateView(UpdateView):
    model = Client
    template_name = "update.html"
    fields = ['name', 'phone', 'annotations']
    
class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('list.html')