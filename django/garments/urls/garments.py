from django.urls import path

from garments import views

app_name = "garments"

urlpatterns = [
    path("", views.GarmentListView.as_view(), name="list"),
    path("<uuid:pk>/", views.GarmentDetailView.as_view(), name="detail"),
    path("create/", views.GarmentCreateView.as_view(), name="create"),
    path("<uuid:pk>/update/", views.GarmentUpdateView.as_view(), name="update"),
]
