from django.urls import path
from category_settings import views

urlpatterns = [
    path('category_settings',  views.test, name='home'),
]
