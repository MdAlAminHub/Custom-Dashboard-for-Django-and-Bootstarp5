from django.db import models


class Categories(models.Model):
    name_english = models.CharField(max_length=50)
    name_bangla= models.CharField(max_length=20)
    image= models.ImageField(
        upload_to='static/assets/images/categories_image', blank=True, null=True)
    icon = models.ImageField(
        upload_to='static/assets/images/categories_icon', blank=True, null=True)
   

    def __str__(self):
       return self.name_english
   
class SubCategories(models.Model):
    category = models.CharField(max_length=100)
    name_english = models.CharField(max_length=50)
    name_bangla= models.CharField(max_length=20)
    
    image= models.ImageField(
        upload_to='static/assets/images/categories_image', blank=True, null=True)
    icon = models.ImageField(
        upload_to='static/assets/images/categories_icon', blank=True, null=True)
   

    def __str__(self):
       return self.category
   
   

