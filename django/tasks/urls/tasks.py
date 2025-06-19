from django.urls import path
from tasks.views.tasks import TaskCreateView
from tasks.views.tasks import TaskDetailView
from tasks.views.tasks import TaskListJsonView
from tasks.views.tasks import TaskListView
from tasks.views.tasks import TaskUpdateView

app_name = "tasks"

urlpatterns = [
    path("", TaskListView.as_view(), name="list"),
    path("json/", TaskListJsonView.as_view(), name="json"),
    path("<uuid:pk>/", TaskDetailView.as_view(), name="detail"),
    path("create/", TaskCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", TaskUpdateView.as_view(), name="update"),
]
