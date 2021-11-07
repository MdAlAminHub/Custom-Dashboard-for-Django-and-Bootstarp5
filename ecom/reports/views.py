from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'customers_total_order/index.html')


def sub_test(request):
    return render(request, 'products_liked/index.html')


def stock(request):
    return render(request, 'products_stock/index.html')


def total_purchased(request):
    return render(request, 'total_purchased/index.html')
