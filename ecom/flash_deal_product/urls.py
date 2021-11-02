from django.urls import path
from flash_deal_product import views

urlpatterns = [
    path('flash_deal_product',  views.test, name='home'),
]
