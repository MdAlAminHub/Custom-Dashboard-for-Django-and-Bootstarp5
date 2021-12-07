from django.db import models

class Brand(models.Model):
    brand_title = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='static/assets/images/brand', blank=True, null=True)
    
    page_choice = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = models.CharField(max_length=50, choices=page_choice)

    
   

    def __str__(self):
        return self.brand_title



