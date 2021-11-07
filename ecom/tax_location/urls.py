from django.urls import path
from tax_location import views

urlpatterns = [
    path('countries',  views.test, name='home'),
    path('tax_classes',  views.sub_test, name='home'),
    path('tax_rates',  views.tax_rates, name='home'),
    path('zones',  views.zones, name='home'),
]