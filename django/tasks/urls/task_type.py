from django.urls import path

from orders import views

app_name = "task_types"

urlpatterns = [
    path("", views.TaskTypeListView.as_view(), name="list"),
    path("<uuid:pk>/", views.TaskTypeDetailView.as_view(), name="detail"),
    path("create/", views.TaskTypeCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", views.TaskUpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete/", views.TaskTypeDeleteView.as_view(), name="delete"),
]
