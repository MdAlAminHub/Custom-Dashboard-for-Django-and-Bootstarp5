from django.shortcuts import render
# from .models import *


def test(request):
    return render(request, 'products/index.html')


def sub_test(request):
    return render(request, 'product_attributes/index.html')


# def rahim(request):
#     return render(request, 'sub_categories/index.html')


# def test(request):
#     return render(request, 'sub_categories/index.html')
