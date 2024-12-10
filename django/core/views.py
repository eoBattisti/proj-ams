from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeRedirectView(LoginRequiredMixin, RedirectView):
    """
    Redirects the user to the clients list view if he is logged in.
    """

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy("clients:list")
