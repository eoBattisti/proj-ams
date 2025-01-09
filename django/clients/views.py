from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse
from .models import Client
from .forms import ClientForm


class ClientListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "clients/list.html"
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

    def get_success_url(self):
        return reverse("clients/list.html")

class ClientsListView(LoginRequiredMixin, TemplateView):
    template_name = "clients/list.html"
