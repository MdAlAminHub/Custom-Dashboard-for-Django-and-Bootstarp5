from django.db import models


class Special_Product(models.Model):
    products = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    page_choice = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=50, choices=page_choice)

  
    def __str__(self):
       return self.products
