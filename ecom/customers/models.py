from django.db import models


class Customers(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    gender  = models.CharField(max_length=20)

    picture = models.ImageField(
        upload_to='static/assets/images/customers_pic', blank=True, null=True)
    dob= models.DateField()
    telephone  = models.IntegerField(max_length=20)
    fax= models.CharField(max_length=50)
    email_address=models.EmailField(max_length=20)
    password = models.CharField(max_length=100)
    status=models.CharField(max_length=50)

  
    def __str__(self):
       return self.first_name


