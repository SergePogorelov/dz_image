from django.urls import path

from . import views


urlpatterns = [
    path(
        'image-upload/',
        views.ImageAPIView.as_view(),
        name='image-upload',
    ),
]
