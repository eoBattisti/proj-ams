from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.http.response import HttpResponseRedirect
from django.http.response import JsonResponse
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import render_to_string
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
        content_type = ContentType.objects.filter(
            app_label=kwargs["app_label"],
        )

        content_type = ContentType.objects.get(
            app_label=kwargs["app_label"],
            model=kwargs["model"],
        )

        self.model = content_type.model_class()

    def get_success_url(self):
        return reverse_lazy(f"{self.model._meta.app_label}:list")


    def get(self, request, *args, **kwargs):
        self.object = self.model.objects.get(pk=kwargs["pk"])
        context = self.get_context_data(object=self.object, app_label=kwargs["app_label"], model=kwargs["model"])

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            html_form = render_to_string(self.template_name, context, request=request)
            return JsonResponse({"html_form": html_form})

        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"success": True, "redirect_url": success_url})

        return HttpResponseRedirect(success_url)
