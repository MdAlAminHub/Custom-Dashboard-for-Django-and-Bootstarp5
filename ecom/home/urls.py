from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('category', views.category, name='category'),
    path('my-profile.html', views.profile, name='profile'),
]