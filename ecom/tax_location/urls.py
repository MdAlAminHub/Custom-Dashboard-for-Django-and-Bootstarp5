from django.urls import path
from tax_location import views

urlpatterns = [
    # path('countries',  views.test, name='home'),
    path('tax_classes',  views.sub_test, name='home'),
    path('tax_classes-list',  views.sub_list, name='t_list'),
    path('tax_rates',  views.test, name='home'),
    path('tax_rates-list',  views.test_list, name='tr_list'),
    # path('zones',  views.zones, name='home'),
]
