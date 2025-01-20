from django.urls import path

from tasks.views.task_type import (
    TaskTypeCreateView,
    TaskTypeDeleteView,
    TaskTypeDetailView,
    TaskTypeListView,
    TaskTypeUpdateView,
)


app_name = "task_types"

urlpatterns = [
    path("", TaskTypeListView.as_view(), name="list"),
    path("<uuid:pk>/", TaskTypeDetailView.as_view(), name="detail"),
    path("create/", TaskTypeCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", TaskTypeUpdateView.as_view(), name="update"),
    path("<uuid:pk>/delete/", TaskTypeDeleteView.as_view(), name="delete"),
]
