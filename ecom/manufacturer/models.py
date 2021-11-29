from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    manufacturer_url = models.CharField(max_length=50)
    image= models.ImageField(
        upload_to='manufacturer' ,blank=True) 
    

    def __str__(self):
       return self.name
