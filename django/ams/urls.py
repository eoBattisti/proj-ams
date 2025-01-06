from django.contrib import admin
from django.urls import path, include

from core.views import HomeRedirectView

urlpatterns = [
    path("", HomeRedirectView.as_view(), name="home"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("clients/", include("clients.urls")),
    path("garments/", include("garments.urls.garments")),
    path("materials/", include("garments.urls.materials")),
    path("orders/", include("orders.urls.orders")),
    path("order-types/", include("orders.urls.order_types")),
    path("tasks/", include("tasks.urls.tasks")),
    path("task-types/", include("tasks.urls.task_types")),
    path("sales/", include("sales.urls")),
]