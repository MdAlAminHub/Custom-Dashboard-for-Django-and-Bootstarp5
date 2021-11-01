from django.urls import path
from packages_subscriptions import views

urlpatterns = [
    path('packages_subscriptions',  views.test, name='home'),
]
