from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    manufacturer_url = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(
        upload_to='static/media/manufacture_images', blank=True, null=True)
    

    def __str__(self):
       return self.name
