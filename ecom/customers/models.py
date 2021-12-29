from django.db import models


class Customers(models.Model):
    username = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    telephone  = models.IntegerField()
    email_address=models.EmailField(max_length=200)
    password = models.CharField(max_length=100)
    conf_password = models.CharField(max_length=100)
   

  
    def __str__(self):
       return self.username


# class Customers(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=20)
#     gender = models.CharField(max_length=20, blank=True, null=True)

#     picture = models.ImageField(
#         upload_to='static/assets/images/customers_pic', blank=True, null=True)
#     dob = models.DateField()
#     telephone = models.IntegerField()
#     email_address = models.EmailField(max_length=20)
#     password = models.CharField(max_length=100)
#     status = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#        return self.first_name

