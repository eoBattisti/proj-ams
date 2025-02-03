from clients.views import ClientCreateView
from clients.views import ClientDeleteView
from clients.views import ClientDetailView
from clients.views import ClientListJsonView
from clients.views import ClientListView
from clients.views import ClientUpdateView
from django.urls import path

app_name = "clients"

urlpatterns = [
    path("", ClientListView.as_view(), name="list"),
    path("json/", ClientListJsonView.as_view(), name="json"),
    path("<uuid:pk>/", ClientDetailView.as_view(), name="detail"),
    path("create/", ClientCreateView.as_view(), name="create"),
    path("update/<uuid:pk>/", ClientUpdateView.as_view(), name="update"),
    path("delete/<uuid:pk>/", ClientDeleteView.as_view(), name="delete"),
]
