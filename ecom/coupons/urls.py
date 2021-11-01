from django.urls import path
from coupons import views

urlpatterns = [
    path('coupons',  views.test, name='home'),
]
