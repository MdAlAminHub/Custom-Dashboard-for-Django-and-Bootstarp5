from django.db import models


class Countries(models.Model):
    country_name = models.CharField(max_length=50)
    iso_code2= models.CharField(max_length=20)
    iso_code3 = models.CharField(max_length=20)

   
    def __str__(self):
       return self.country_name


class TaxClasses(models.Model):
    title= models.CharField(max_length=100)
    descriptiom = models.CharField(max_length=50)
    

    def __str__(self):
       return self.title


class TaxRates(models.Model):
    tax_class= models.CharField(max_length=100)
    zone = models.CharField(max_length=50)
    tax_rate=models.IntegerField(max_length=50)
    descriptiom = models.CharField(max_length=50)


    def __str__(self):
       return self.tax_class
   
class Zones(models.Model):
    country= models.CharField(max_length=100)
    country_name = models.CharField(max_length=50)
    country_code = models.IntegerField(max_length=50)
    


    def __str__(self):
       return self.country
