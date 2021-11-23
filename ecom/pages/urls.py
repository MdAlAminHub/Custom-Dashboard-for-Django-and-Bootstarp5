from django.urls import path
from pages import views

urlpatterns = [
    path('pages',  views.test, name='home'),
    path('Pages-list',  views.list, name='p_list'),
    
]
