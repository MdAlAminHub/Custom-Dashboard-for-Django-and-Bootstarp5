from django.contrib import admin
from django.urls import path,include 

urlpatterns = [
    path('home/', include('home.urls')),
    path('home/', include('brand.urls')),
    path('home/', include('manufacturer.urls')),
    path('home/', include('category.urls')),
    path('home/', include('languages.urls')),
    path('home/', include('pages.urls')),
    path('home/', include('coupons.urls')),
    path('home/', include('customers.urls')),
    path('home/', include('orders.urls')),
    path('home/', include('packages_subscriptions.urls')),
    



    # path('admin/', admin.site.urls),
]

