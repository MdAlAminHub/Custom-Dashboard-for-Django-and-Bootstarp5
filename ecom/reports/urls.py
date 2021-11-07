from django.urls import path
from reports import views

urlpatterns = [
    path('customers_total_order',  views.test, name='home'),
    path('products_liked',  views.sub_test, name='home'),
    path('products_stock',  views.stock, name='home'),
    path('total_purchased',  views.total_purchased, name='home'),
]
