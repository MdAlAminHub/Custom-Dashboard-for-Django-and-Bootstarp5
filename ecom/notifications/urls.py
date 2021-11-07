from django.urls import path
from notifications import views

urlpatterns = [
    path('devices',  views.test, name='home'),
    path('send_notifications',  views.sub_test, name='home'),
    # path('sub-sub-categories',  views.rahim, name='home'),
    # path('/sub_categories',  views.test, name='home'),
]
