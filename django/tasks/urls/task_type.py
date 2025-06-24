from django.urls import path
from tasks.views.task_type import TaskTypeCreateView
from tasks.views.task_type import TaskTypeListHTMXView
from tasks.views.task_type import TaskTypeDetailView
from tasks.views.task_type import TaskTypeHTMXStatsView
from tasks.views.task_type import TaskTypeListView
from tasks.views.task_type import TaskTypeUpdateView

app_name = "task_types"

urlpatterns = [
    path("", TaskTypeListView.as_view(), name="list"),
    path("htmx/", TaskTypeListHTMXView.as_view(), name="htmx"),
    path("stats/", TaskTypeHTMXStatsView.as_view(), name="stats"),
    path("<uuid:pk>/", TaskTypeDetailView.as_view(), name="detail"),
    path("create/", TaskTypeCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", TaskTypeUpdateView.as_view(), name="update"),
]
