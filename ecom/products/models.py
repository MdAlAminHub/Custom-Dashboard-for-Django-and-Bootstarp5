from django.db import models


class Product(models.Model):
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=20)
    manufacturars= models.CharField(max_length=50)
    special = models.CharField(max_length=20)
    product_name_english = models.CharField(max_length=50)
    description_english = models.CharField(max_length=50)
    product_name_bangla = models.CharField(max_length=20)
    description_bangla = models.CharField(max_length=50)
    tax_class= models.CharField(max_length=50)
    product_price= models.IntegerField(max_length=20)
    product_weight = models.IntegerField(
        max_length=20), models.CharField(max_length=50)
    products_quantity=models.IntegerField(max_length=100)
    offer_quantity_limit = models.IntegerField(max_length=100)
    quantity_low_limit = models.IntegerField(max_length=100)
    image = models.ImageField(
        upload_to='static/assets/images/products_image', blank=True, null=True)
    status = models.CharField(max_length=50)
    

    def __str__(self):
       return self.name
   
class ProductAttributes(models.Model):
    add_options_english = models.CharField(max_length=50)
    add_options_bangla= models.CharField(max_length=20)

    def __str__(self):
       return self.name
