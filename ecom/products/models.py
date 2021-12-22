# from django.db import models
# from categories.models import Categories, SubCategories, SubCategories_2


# class Product(models.Model):
#     category = models.ForeignKey(Categories, on_delete=models.CASCADE)
#     subcategory = models.ForeignKey(SubCategories, on_delete=models.CASCADE, blank=True, null=True)
#     subcategory_2 = models.ForeignKey(
#         SubCategories_2, on_delete=models.CASCADE, blank=True, null=True)
#     manufacturars= models.CharField(max_length=50)
#     special = models.CharField(max_length=20, blank=True, null=True)
#     product_name_english = models.CharField(max_length=50)
#     description_english = models.TextField()
#     product_name_bangla = models.CharField(max_length=20)
#     description_bangla = models.TextField()
#     tax_class = models.CharField(max_length=50, blank=True, null=True)
#     product_price= models.IntegerField()
#     product_weight = models.IntegerField(), models.CharField(max_length=50)
#     products_quantity = models.IntegerField(blank=True, null=True)
#     offer_quantity_limit = models.IntegerField(blank=True, null=True)
#     quantity_low_limit = models.IntegerField(blank=True, null=True)
#     image = models.ImageField(
#         upload_to='static/assets/images/products_image', blank=True, null=True)
#     status = models.CharField(max_length=50, blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)
    

#     def __str__(self):
#        return self.product_name_english 
   
# class ProductAttributes(models.Model):
#     add_options_english = models.CharField(max_length=50)
#     add_options_bangla= models.CharField(max_length=20)

#     def __str__(self):
#        return self.add_options_english
