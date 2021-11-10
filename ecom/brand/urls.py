from languages import views
from django.urls import path
from brand import views


urlpatterns = [
    path('brand',  views.test, name='home'),
    path('brand-list',  views.list, name='b_list'),
]

