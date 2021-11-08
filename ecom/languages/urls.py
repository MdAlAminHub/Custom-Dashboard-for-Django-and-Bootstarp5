from django.urls import path
from languages import views

urlpatterns = [
    path('languages',  views.test, name='home'),
    path('languages-list',  views.list, name='l_list'),
]
