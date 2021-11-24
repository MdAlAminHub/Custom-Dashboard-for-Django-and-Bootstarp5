from django.db import models


class Packages(models.Model):
    package_name = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.ImageField(
        upload_to='static/assets/images/package_images', blank=True, null=True)
    slider = models.ImageField(
        upload_to='static/assets/images/package_images', blank=True, null=True)
    feature = models.CharField(max_length=50)
    

    def __str__(self):
       return self.name


class PackagesType(models.Model):
    package_type_name= models.CharField(max_length=50)
    add_options_bangla = models.CharField(max_length=20)
    cashback= models.IntegerField()
    nb_card_limit= models.IntegerField()
    monthly_target= models.IntegerField()
   
    delivary_prority = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to='static/assets/images/package_images', blank=True, null=True)

    def __str__(self):
       return self.name


class PackagesTypeAttributes(models.Model):
    name = models.CharField(max_length=50)
    # option=models.
    def __str__(self):
       return self.name