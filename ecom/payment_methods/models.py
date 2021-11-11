from django.db import models


class PaymentMethods(models.Model):
    
    payment_methods = models.CharField(max_length=50)
    braintree_account_type = models.CharField(max_length=20)
    braintree = models.CharField(max_length=20)
    marchant_id = models.CharField(max_length=50)
    private_key = models.CharField(max_length=20)
    public_key = models.CharField(max_length=20)
    stripe_environment = models.CharField(max_length=20)
    stripe = models.CharField(max_length=20)
    secret_key = models.CharField(max_length=20)
    key = models.CharField(max_length=20)
    paypal_environment = models.CharField(max_length=20)
    paypal = models.CharField(max_length=20)
    paypal_id = models.CharField(max_length=20)
    cash_on_delivary = models.CharField(max_length=20)
    payment_in_currency = models.CharField(max_length=20)

    
    def __str__(self):
       return self.payment_methods


