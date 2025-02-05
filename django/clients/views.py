import json
from typing import Any

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import QuerySet
from django.http import HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from .forms import ClientForm
from .models import Client


class ClientListView(LoginRequiredMixin, TemplateView):
    template_name = "clients/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_clients"] = Client.objects.count()
        return context


class ClientListJsonView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        objects: QuerySet[Client, Client] = super().get_queryset()
        return objects

    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        page_number = self.request.GET.get('page', 1)
        page_size = self.request.GET.get('pageSize', 10)

        paginator = Paginator(self.get_queryset(), page_size)
        page_obj = paginator.get_page(page_number)

        # Prepare data for Grid.js
        data = [{
            'name': client.name,
            'phone': client.phone,
            'annotations': client.annotations,
            'address': str(client.address),
        } for client in page_obj]

        response_data = {
            'data': data,
            'total': paginator.count,
        }

        return HttpResponse(
            json.dumps(response_data), 
            content_type='application/json'
        )


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "clients/detail.html"
    context_object_name = "client"


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "clients/form.html"
    form_class = ClientForm
    success_url = reverse_lazy("clients:list")


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = "clients/form.html"
    form_class = ClientForm
    success_url = reverse_lazy("clients:list")


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client

    def get_success_url(self):
        return reverse("clients/list.html")


class ClientsListView(LoginRequiredMixin, TemplateView):
    template_name = "clients/list.html"
