from django.db import models

class Brand(models.Model):
    brand_title = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='static/assets/images/brand', blank=True, null=True)
    
   

    def __str__(self):
        return self.brand_title



