from django.urls import path
from pages import views

urlpatterns = [
    path('pages',  views.test, name='home'),
    path('Pages-list',  views.list, name='p_list'),
    path('dalete/<int:id>/',  views.delete_data, name="deletedata"),
    path('/<int:id>/',  views.update_pages, name="update_pages"),

    

]
