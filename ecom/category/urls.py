from django.urls import path
from category import views

urlpatterns = [
    path('category',  views.category, name='home'),
]
