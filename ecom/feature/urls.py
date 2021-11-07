from django.urls import path
from feature import views

urlpatterns = [
    path('create_feature',  views.test, name='home'),
    path('manage_feature',  views.sub_test, name='home'),
    # path('sub-sub-categories',  views.rahim, name='home'),
    # path('/sub_categories',  views.test, name='home'),
]
