
from PIL import Image as PilImage
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from images.models import Image


class ImageAPIView(APIView):

    def post(self, request, *args, **kwargs):
        image_file = request.FILES.get('file')
        img = Image.objects.create(image=image_file)

        with PilImage.open(img.image.path) as im:
            (width, height) = (im.width // 2, im.height // 2)
            im.resize((width, height)).rotate(angle=45).save(img.image.path)

        return Response({'status':'ok'}, status=status.HTTP_201_CREATED)
