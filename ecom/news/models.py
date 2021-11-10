from django.db import models


class News(models.Model):
    category = models.CharField(max_length=50)
    title_new_english = models.CharField(max_length=20)
    description_english = models.CharField(max_length=20)
    title_new_bangla= models.CharField(max_length=20)
    description_bangla = models.CharField(max_length=20)
    image = models.ImageField(
        upload_to='static/assets/images/news_images', blank=True, null=True)
    is_feature = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
       return self.name


class NewsCategories(models.Model):
    name_english = models.CharField(max_length=100)
    name_bangla = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='static/assets/images/news_images', blank=True, null=True)
    

    def __str__(self):
       return self.name
