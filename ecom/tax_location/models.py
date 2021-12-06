from django.db import models
from .models import *


# class Countries(models.Model):
#     country_name = models.CharField(max_length=50)
#     iso_code2= models.CharField(max_length=20)
#     iso_code3 = models.CharField(max_length=20)

   
#     def __str__(self):
#        return self.country_name


class TaxClasses(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    

    def __str__(self):
       return self.title


class TaxRates(models.Model):
    #table column name = form input name 
    tax_classes = models.ForeignKey(TaxClasses, on_delete=models.CASCADE)
    tax_class = models.CharField(max_length=50)
    # zone = models.CharField(max_length=50)
    tax_rate=models.IntegerField()
    description = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    


    def __str__(self):
       return self.tax_class
   
# class Zones(models.Model):
#     country= models.CharField(max_length=100)
#     country_name = models.CharField(max_length=50)
#     country_code = models.IntegerField()
    


#     def __str__(self):
#        return self.country
