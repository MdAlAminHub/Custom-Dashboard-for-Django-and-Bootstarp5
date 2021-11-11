from django.db import models


class Coupons(models.Model):
    coupon = models.CharField(max_length=50)
    desc= models.TextField()
    coupon_type = models.CharField(max_length=50)
    discount_type = models.CharField(max_length=50)
    coupon_ammount=models.IntegerField(max_length=50)
    coupon_expiry_date=models.DateField
    minimum_spend = models.IntegerField(max_length=50)
    coupon_quantity_limit = models.IntegerField(max_length=50)
    products = models.CharField(max_length=500)
    exclude_products = models.CharField(max_length=500)
    usage_limit_per_coupon = models.IntegerField(max_length=50)
    usage_limit_per_user = models.IntegerField(max_length=50)
    
    

   
    def __str__(self):
       return self.coupon

