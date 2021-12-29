from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"), 
 
    path('customer',  views.customer_detail, name='store/main.html'),
    
	path('signup/', views.signup_view, name="signup"),
	path('login/', views.login_view, name="login"),
	path('logout/', views.logout_view, name="logout"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
    path('sub_categories_obj/', views.get_general_product,
         name="sub_categories_obj"),
    path('get_cooking_essentials/', views.get_cooking_essentials,
         name="get_cooking_essentials"),
    path('get_home_care/', views.get_home_care,
         name="get_home_care"),
    path('filter_products/<int:id>/', views.get_filterd_product, name='filter_products')

]
