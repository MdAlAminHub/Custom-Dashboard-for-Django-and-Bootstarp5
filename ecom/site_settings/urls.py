from django.urls import path
from site_settings import views

urlpatterns = [
    path('order_status',  views.test, name='home'),
    path('settings',  views.sub_test, name='home'),
    # path('sub-sub-categories',  views.rahim, name='home'),
    # path('/sub_categories',  views.test, name='home'),
]
