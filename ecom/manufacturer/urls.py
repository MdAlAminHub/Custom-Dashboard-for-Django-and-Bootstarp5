from pages import views
from django.urls import path
from manufacturer import views

urlpatterns = [
    path('manufacturer',  views.test, name='home'),
    # path('manufacturer-list',  views.list, name='m_list'),
    # path('manufacturer-list',  views.list, name='m_list'),
]

