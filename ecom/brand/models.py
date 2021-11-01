from django.db import models
from django.utils.text import slugify

# Create your models here.
class Brand(models.Model):
    brand_title=models.CharField(max_length=50)
    image = models.ImageField(upload_to='static/assets/images/brand')
    slug = models.SlugField(max_length=200, blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.brand_title)
        # super(Brand,self).save(*args, **kwargs)

    def __str__(self):
        return self.brand


class BrandImages(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='static/assets/images/brand')
