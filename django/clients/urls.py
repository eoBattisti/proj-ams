from django.urls import path

from clients.views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, client_list
from clients import views

app_name = "clients"

urlpatterns = [
    path('clients/', ClientListView.as_view(), name = "list"),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name = "detail"),
    path('clients/create', ClientCreateView.as_view(), name = "create"),
    path('clients/<int:pk>/update', ClientUpdateView.as_view(), name = "update"),
    path('clients/<int:pk>/delete', ClientDeleteView.as_view(), name = "delete"),    
]
