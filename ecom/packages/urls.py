from django.urls import path
from packages import views

urlpatterns = [
    path('packages',  views.test, name='home'),
    path('packages_type',  views.sub_test, name='home'),
    path('packages_type_attribute',  views.sub_type_test, name='home'),
    # path('/sub_categories',  views.test, name='home'),
]
