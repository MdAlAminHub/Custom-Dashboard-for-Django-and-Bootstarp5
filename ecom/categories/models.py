from django.db import models


class Categories(models.Model):
    name_english = models.CharField(max_length=70)
    name_bangla= models.CharField(max_length=70)
    image= models.ImageField(
        upload_to='static/assets/images/categories_image', blank=True, null=True)
    icon = models.ImageField(
        upload_to='static/assets/images/categories_icon', blank=True, null=True)
    
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
   

    def __str__(self):
       return self.name_english
   
class SubCategories(models.Model):
    category= models.ForeignKey(Categories, on_delete=models.CASCADE)
    name_english = models.CharField(max_length=70)
    name_bangla= models.CharField(max_length=70)
    
    image= models.ImageField(
        upload_to='static/assets/images/categories_image', blank=True, null=True)
    icon = models.ImageField(
        upload_to='static/assets/images/categories_icon', blank=True, null=True)
   

    def __str__(self):
       return self.category
   
   
class SubCategories_2(models.Model):
    category = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    name_english = models.CharField(max_length=70)
    name_bangla = models.CharField(max_length=70)

    image = models.ImageField(
        upload_to='static/assets/images/categories_image', blank=True, null=True)
    icon = models.ImageField(
        upload_to='static/assets/images/categories_icon', blank=True, null=True)

    def __str__(self):
       return self.category
   
   

