from django.urls import path
from categories import views

urlpatterns = [
    path('categories',  views.test, name='home'),
    path('sub-categories',  views.sub_test, name='home'),
    # path('sub-sub-categories',  views.rahim, name='home'),
    # path('/sub_categories',  views.test, name='home'),
]
