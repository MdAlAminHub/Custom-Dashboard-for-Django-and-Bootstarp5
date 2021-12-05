from django.urls import path
from special_product import views

urlpatterns = [
    path('special_product',  views.test, name='home'),
    path('special_product-list',  views.sub_list, name='sp_list'),
]
