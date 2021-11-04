from django.urls import path
from categories import views

urlpatterns = [
    path('categories/categories',  views.test, name='home'),
    path('categories/sub_categories',  views.test, name='home'),
]
