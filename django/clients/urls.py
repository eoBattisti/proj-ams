from django.urls import path

from .views import ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView, client_list
from clients import views

app_name = 'clients'

urlpatterns = [
    # path('', views.ClientsListView.as_view(), name='list'),
    path('clients/', ClientListView.as_view(), name = "list"),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name = "client_detail"),
    path('clients/create', ClientCreateView.as_view(), name = "client_create"),
    path('clients/<int:pk>/update', ClientUpdateView.as_view(), name = "client_update"),
    path('clients/<int:pk>/delete', ClientDeleteView.as_view(), name = "client_delete"),
    path('test/', client_list, name = "")
    
]
