from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView

from .models import Image


class ImageListView(ListView):
    model = Image


class ImageDetailView(DetailView):
    model = Image
