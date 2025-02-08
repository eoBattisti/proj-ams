from django.urls import path
from orders import views

app_name = "orders"

urlpatterns = [
    path("", views.OrderListView.as_view(), name="list"),
    path("json/", views.OrderListJsonView.as_view(), name="json"),
    path("<uuid:pk>/", views.OrderDetailView.as_view(), name="detail"),
    path("create/", views.OrderCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", views.OrderUpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete/", views.OrderDeleteView.as_view(), name="delete"),
]
