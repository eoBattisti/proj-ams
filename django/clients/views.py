from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class ClientsListView(LoginRequiredMixin, TemplateView):
    template_name = 'clients/list.html'
