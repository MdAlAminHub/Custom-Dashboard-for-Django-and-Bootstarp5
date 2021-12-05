from django.db import models


class Special_Product(models.Model):
    products = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

  
    def __str__(self):
       return self.products
