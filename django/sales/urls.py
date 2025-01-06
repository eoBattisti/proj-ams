from django.urls import path

from sales import views


app_name = "sales"

urlpatterns = [
    path("", views.SaleListView.as_view(), name="list"),
    path("<uuid:pk>/", views.SaleDetailView.as_view(), name="detail"),
    path("create/", views.SaleCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", views.SaleUpdateView.as_view(), name="update"),
]

