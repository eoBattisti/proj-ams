from django.urls import path

from garments import views


app_name = "materials"

urlpatterns = [
    path("", views.MaterialListView.as_view(), name="list"),
    path("<uuid:pk>/", views.MaterialDetailView.as_view(), name="detail"),
    path("create/", views.MaterialCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", views.MaterialUpdateView.as_view(), name="update"),
]
