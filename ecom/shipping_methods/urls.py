from django.urls import path
from shipping_methods import views

urlpatterns = [
    path('shipping_methods',  views.test, name='home'),
]
