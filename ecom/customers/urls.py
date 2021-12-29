from django.urls import path
from customers import views

urlpatterns = [
    path('customers',  views.test, name='store/main.html'),
    # path('customers-list',  views.list, name='c_list'),
]
