from django.urls import path
from manufacturer import views

urlpatterns = [
    path('manufacturer',  views.test, name='home'),
]
