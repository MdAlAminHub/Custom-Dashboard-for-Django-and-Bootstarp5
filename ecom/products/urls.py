from django.urls import path
from products import views

urlpatterns = [
    path('products',  views.test, name='home'),
    path('product_attributes',  views.sub_test, name='home'),
    path('product_attributes-list',  views.sub_test, name='home'),
    path('products-list',  views.list, name='p_list'),
  
]
