from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView
from django.views.generic import RedirectView


class HomeRedirectView(LoginRequiredMixin, RedirectView):
    """
    Redirects the user to the clients list view if he is logged in.
    """

    def get_redirect_url(self, *args, **kwargs):
        return reverse_lazy("clients:list")


class GenericDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "components/delete_modal.html"

    def setup(self, request, *args, **kwargs):
        super().setup(request, *args, **kwargs)
        print(kwargs)
        content_type = ContentType.objects.get(
            app_label=kwargs["app_label"],
            model=kwargs["model"],
        )
        self.model = content_type.model_class()

    def get_success_url(self):
        return reverse_lazy(f"{self.model._meta.app_label}:htmx")

    def form_valid(self, form):
        try:
            if not self._is_htmx_request():
                return super().form_valid(form)

            print(self.object)
            success_url = self.get_success_url()
            self.object.delete()
            response = HttpResponse(success_url)
            response["HX-Trigger"] = "closeModal"
            return response

        except Exception as e:
            print(e)
        return super().form_valid(form)

    def _is_htmx_request(self):
        return self.request.headers.get("HX-Request") == "true"

    def get(self, request, *args, **kwargs):
        self.object = self.model.objects.get(pk=kwargs["pk"])
        context = self.get_context_data(
            object=self.object,
            app_label=kwargs["app_label"],
            model=kwargs["model"]
        )

        return self.render_to_response(context)
