from django.urls import path
from languages import views

urlpatterns = [
    path('languages',  views.test, name='home'),
]
