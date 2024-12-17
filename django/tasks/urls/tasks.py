from django.urls import path

from tasks import views

app_name = "tasks"

urlpatterns = [
    path("", views.TaskListView.as_view(), name="list"),
    path("<uuid:pk>/", views.TaskDetailView.as_view(), name="detail"),
    path("create/", views.TaskCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", views.TaskUpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete/", views.TaskDeleteView.as_view(), name="delete"),
]
