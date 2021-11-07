from django.urls import path
from news import views

urlpatterns = [
    path('news',  views.test, name='home'),
    path('news_categories',  views.sub_test, name='home'),
    # path('sub-sub-categories',  views.rahim, name='home'),
    # path('/sub_categories',  views.test, name='home'),
]
