from django.urls import path

from orders import views

app_name = "order_types"

urlpatterns = [
    path("", views.OrderTypeListView.as_view(), name="list"),
    path("<uuid:pk>/", views.OrderTypeDetailView.as_view(), name="detail"),
    path("create/", views.OrderTypeCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", views.OrderUpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete/", views.OrderTypeDeleteView.as_view(), name="delete"),
]
