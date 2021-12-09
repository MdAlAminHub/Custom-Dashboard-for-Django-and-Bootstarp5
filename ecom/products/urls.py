from django.urls import path
from . import views

urlpatterns = [
    path('products',  views.TEST, name='home'),
    path('product_attributes',  views.sub_test, name='home'),
    path('product_attributes-list',  views.sub_list, name='home'),
    path('products-list',  views.list, name='p_list'),
    path('dalete/<int:id>/',  views.delete_products, name="delete_product"),
    path('/<int:id>/',  views.update_products, name="update_products"),
]
