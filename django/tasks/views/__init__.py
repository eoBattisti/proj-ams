from tasks.views.tasks import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView
from tasks.views.task_type import (
    TaskTypeDeleteView,
    TaskTypeListView,
    TaskTypeDetailView,
    TaskTypeCreateView,
    TaskTypeUpdateView,
)


__all__ = [
    "TaskListView",
    "TaskDetailView",
    "TaskCreateView",
    "TaskUpdateView",
    "TaskTypeListView",
    "TaskTypeDetailView",
    "TaskTypeCreateView",
    "TaskTypeUpdateView",
    "TaskDeleteView",
    "TaskTypeDeleteView",
]
