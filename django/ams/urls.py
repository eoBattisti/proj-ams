from core.views import GenericDeleteView
from core.views import HomeRedirectView
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    path("", HomeRedirectView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("clients/", include("clients.urls")),
    path("delete/<str:app_label>/<str:model>/<uuid:pk>/", GenericDeleteView.as_view(), name="delete"),
    path("orders/", include("orders.urls.orders")),
    path("tasks/", include("tasks.urls.tasks")),
    path("task-types/", include("tasks.urls.task_type")),
]
