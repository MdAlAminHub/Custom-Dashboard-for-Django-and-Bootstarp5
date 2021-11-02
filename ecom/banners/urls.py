from django.urls import path
from banners import views

urlpatterns = [
    path('banners',  views.test, name='home'),
]
