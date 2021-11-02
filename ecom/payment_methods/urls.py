from django.urls import path
from payment_methods import views

urlpatterns = [
    path('payment_methods',  views.test, name='home'),
]
