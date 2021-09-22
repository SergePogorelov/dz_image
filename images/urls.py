from django.urls import path

from . import views


app_name = "images"

urlpatterns = [
    path("detail/<int:pk>/", views.ImageDetailView.as_view(), name="detail"),
    path("", views.ImageListView.as_view(), name="index"),
]
