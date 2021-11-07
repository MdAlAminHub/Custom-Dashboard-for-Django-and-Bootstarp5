from django.urls import path
from products import views

urlpatterns = [
    path('products',  views.test, name='home'),
    path('product_attributes',  views.sub_test, name='home'),
    #path('sub-sub-categories',  views.rahim, name='home'),
    # path('/sub_categories',  views.test, name='home'),
]
