from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView

from .models import Image


class ImageListView(ListView):
    model = Image


class ImageDetailView(DetailView):
    model = Image

class ImageTemplateView(TemplateView):
    template_name = 'images/image_form.html'
