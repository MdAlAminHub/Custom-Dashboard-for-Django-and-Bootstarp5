from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('', views.brand, name='brand'),
    # path('my-profile.html', views.profile, name='profile'),
]