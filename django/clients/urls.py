from django.urls import path

from clients.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView

app_name = "clients"

urlpatterns = [
    path("", ClientListView.as_view(), name="list"),
    path("<uuid:pk>/", ClientDetailView.as_view(), name="detail"),
    path("create/", ClientCreateView.as_view(), name="create"),
    path("update/<uuid:pk>/", ClientUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>/", ClientDeleteView.as_view(), name="delete"),
]
