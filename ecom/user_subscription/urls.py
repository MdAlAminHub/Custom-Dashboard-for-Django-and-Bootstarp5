from django.urls import path
from user_subscription import views

urlpatterns = [
    path('user_subscription',  views.test, name='home'),
]
