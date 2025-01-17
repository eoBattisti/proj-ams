from django.urls import path

from tasks.views.tasks import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="list"),
    path("<uuid:pk>/", TaskDetailView.as_view(), name="detail"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", TaskUpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete/", TaskDeleteView.as_view(), name="delete"),
]
