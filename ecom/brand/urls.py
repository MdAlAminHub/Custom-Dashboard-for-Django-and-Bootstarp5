from django.urls import path
from brand import views


urlpatterns = [
    path('brand',  views.index, name='home'),
]
