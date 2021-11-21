from django.urls import path
from categories import views


urlpatterns = [
    path('categories',  views.test, name='home'),
    path('categories-list',  views.list, name='c_list'),
    path('sub_categories-list',  views.sub_list, name='sub_c_list'),
    path('sub_categories',  views.sub_test, name='home'),
    path('dalete/<int:id>/',  views.delete_data, name="deletedata"),
    
]
