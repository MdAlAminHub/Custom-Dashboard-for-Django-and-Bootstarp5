from django.urls import path
from categories import views


urlpatterns = [
    path('categories',  views.test, name='home'),
    path('categories-list',  views.list, name='c_list'),
    path('sub_categories-list',  views.sub_list, name='sub_c_list'),
    path('sub_categories_2-list',  views.sub_list_2, name='sub_c_2_list'),
    path('sub_categories',  views.sub_test, name='home'),
    path('sub_categories_2',  views.sub_test_2, name='home'),
    path('dalete/<int:id>/',  views.delete_data, name="deletedata"),
    
]
