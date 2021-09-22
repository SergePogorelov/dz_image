from django.urls import path

from . import views


app_name = "images"

urlpatterns = [
    path("list/", views.ImageListView.as_view(), name="list"),
    path("detail/<int:pk>/", views.ImageDetailView.as_view(), name="detail"),
    path("", views.ImageTemplateView.as_view(), name="upload"),
]
