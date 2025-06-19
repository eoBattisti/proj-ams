import datetime as dt
from zoneinfo import ZoneInfo
from dateutil.relativedelta import relativedelta

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from .forms import ClientForm
from .models import Client


class ClientListView(LoginRequiredMixin, TemplateView):
    template_name = "clients/list.html"


class ClientStatsHTMXView(LoginRequiredMixin, TemplateView):
    template_name = "clients/components/stats.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_clients = Client.objects.all()
        last_moth = dt.datetime.now(tz=ZoneInfo(settings.TIME_ZONE)).date() - relativedelta(months=1)

        context["total_clients"] = total_clients.count()
        context["total_new_clients"] = total_clients.filter(created_at__gte=last_moth).count()

        return context


class ClientListHTMXView(LoginRequiredMixin, ListView):
    model = Client
    template_name = "clients/components/rows.html"
    context_object_name = "clients"


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = "clients/detail.html"
    context_object_name = "client"


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = "clients/form.html"
    form_class = ClientForm
    success_url = reverse_lazy("clients:htmx")

    def form_valid(self, form):
        try:
            self.object = form.save()
            if not self._is_htmx_request():
                return super().form_valid(form)

            response = HttpResponse()
            response["HX-Trigger"] = "closeModal"
            return response

        except Exception as e:
            print(e)

    def _is_htmx_request(self):
        return self.request.headers.get("HX-Request") == "true"


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = "clients/form.html"
    form_class = ClientForm
    success_url = reverse_lazy("clients:htmx")

    def form_valid(self, form):
        try:
            self.object = form.save()
            if not self._is_htmx_request():
                return super().form_valid(form)

            response = HttpResponse()
            response["HX-Trigger"] = "closeModal"
            return response

        except Exception as e:
            print(e)

    def _is_htmx_request(self):
        return self.request.headers.get("HX-Request") == "true"
