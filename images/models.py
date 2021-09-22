from django.db import models


class Image(models.Model):
    image = models.ImageField('Изображение', upload_to='')

    class Meta:
        ordering = ('-pk',)

    def __str__(self):
        return f'{self.image.name}'
